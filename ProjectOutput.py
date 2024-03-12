# Quentin Hardison

import csv

class ProcessedInventoryReport:
    """
    This class processed the data stored in Inventory instance,
    and writes reports into csv
        There are 4 reports to be written:
                1. Full Inventory Report
                2. Item Type Inventory List Report
                3. Past Service Date Inventory Report
                4. Damaged Inventory Report
    """
    # Creates ProcessedInventoryReport class with Inventory as its properties
    def __init__(self, inventory):
        self.inventory = inventory


    def write_full_inventory_report(self, filename):
        """
        This function lists all the items with all their information
        The items are sorted alphabetically by manufacturer name
        The processed data are then written into csv with filename provided as input

        Parameter:
            filename (str): The name of csv file to be written into (e.g. FullInventory.csv)
        """
        all_manufacturers = self.inventory.get_all_manufacturers()
        # Creates a list to store all manufacturer name
        manufacturer_names = []
        # Repeats through all manufacturers
        for m in all_manufacturers:
            manufacturer_names.append(m.manufacturer_name)
        # Removes duplicated
        manufacturer_names_unique = list(set(manufacturer_names))
        # Sorts alphabetically by manufacturer name
        manufacturer_names_sorted = sorted(manufacturer_names_unique)

        with open(filename, "w", newline="") as fullinventory_csvfile:
            writer = csv.writer(fullinventory_csvfile)
            # Repeats through the sorted manufacturer's name
            for m_name in manufacturer_names_sorted:
                # Gets the list of Manufacturer instances by name
                manufacturers = self.inventory.get_manufacturer_by_name(m_name)
                # Repeat through all manufacturers with similar name
                for manufacturer in manufacturers:
                    # Writes into csv, row-by-row
                    writer.writerow(
                        [
                            manufacturer.item_id,
                            manufacturer.manufacturer_name,
                            manufacturer.item_type,
                            manufacturer.item_price,
                            manufacturer.service_date,
                            manufacturer.damaged_indicator
                        ]
                    )
    
    
    def write_item_type_inventory_list_report(self):
        """
        This function separated the files with item type,
        creating a file for each item type and the item type is in the file name
        The items are sorted by their item ID
        """
        all_manufacturers = self.inventory.get_all_manufacturers()
        # Creates a list to store all manufacturer name
        item_types = []
        # Repeats through all manufacturer
        for m in all_manufacturers:
            item_types.append(m.item_type)
        # Removes duplicated
        item_types_unique = list(set(item_types))

        for item_type in item_types_unique:
            # Capitalizes the first letter. e.g. convert laptop -> Laptop
            first_capital_item_type_name = item_type[0].upper() + item_type[1:]

            with open(f"{first_capital_item_type_name}Inventory.csv", "w", newline="") as itemtypeinventory_csvfile:
                writer = csv.writer(itemtypeinventory_csvfile)

                # Gets list of item_ids for each item_type
                item_ids = []
                manufacturers = self.inventory.get_manufacturer_by_itemtype(item_type)

                for m in manufacturers:
                    item_ids.append(int(m.item_id))

                item_ids_sorted = sorted(item_ids)

                # Repeats through the sorted manufacturer's name
                for item_id in item_ids_sorted:
                    # Gets the Manufacturer instances by item id
                    manufacturer = self.inventory.get_manufacturer(str(item_id))
                    # Writes into csv for each row with sorted item ID
                    writer.writerow(
                        [
                            manufacturer.item_id,
                            manufacturer.manufacturer_name,
                            manufacturer.item_price,
                            manufacturer.service_date,
                            manufacturer.damaged_indicator
                        ]
                    )


    def write_past_service_date_inventory(self, filename):
        """
        This function lists all the items that are past the service date on the day
        the program is actually executed.
        The items are sorted by their service date from oldest to most recent.

        Parameter:
            filename (str): The name of csv file to be written into (e.g. PastServiceDateInventory.csv)
        """
        # The day this program is executed
        from datetime import datetime
        today = datetime.now()
        
        all_manufacturers = self.inventory.get_all_manufacturers()
        # Creates empty list to store date that are not later than today
        expired_dates_formatted = []

        for manufacturer in all_manufacturers:
            service_date_formatted = datetime.strptime(manufacturer.service_date, "%m/%d/%Y")
            if service_date_formatted < today:
                expired_dates_formatted.append(service_date_formatted)
        
        # Sorts service date from oldest to most recent
        expired_dates_sorted = sorted(expired_dates_formatted, reverse=False)

        with open(filename, "w", newline="") as pastservicedateinventory_csvfile:
            writer = csv.writer(pastservicedateinventory_csvfile)

            for expired_date_formatted in expired_dates_sorted:
                # Converts from datetime format into string
                expired_date_string = str(expired_date_formatted.month) + "/" + str(expired_date_formatted.day) + "/" + str(expired_date_formatted.year)
                manufacturers = self.inventory.get_manufacturer_by_servicedate(expired_date_string)

                for manufacturer in manufacturers:
                    # Writes into csv for each row with sorted service dates
                    writer.writerow(
                        [
                            manufacturer.item_id,
                            manufacturer.manufacturer_name,
                            manufacturer.item_type,
                            manufacturer.item_price,
                            manufacturer.service_date,
                            manufacturer.damaged_indicator
                        ]
                    )


    def write_damaged_inventory_report(self, filename):
        """
        This function lists all the items that are damaged.
        The items are sorted by their prices from most expensive to least expensive.

        Parameter:
            filename (str): The name of csv file to be written into (e.g. DamagedInventory.csv)
        """
        manufacturers_by_damaged_indicator = self.inventory.get_any_damaged_indicators("damaged")

        # Creates empty list to store prices of damaged items
        damaged_item_prices = []

        for manufacturer in manufacturers_by_damaged_indicator:
            if manufacturer.damaged_indicator == "damaged":
                damaged_item_prices.append(manufacturer.item_price)

        # Sorts item by price
        damaged_item_prices_sorted = sorted(damaged_item_prices, reverse=True)

        with open(filename, "w", newline="") as damagedinventory_csvfile:
            writer = csv.writer(damagedinventory_csvfile)

            for damaged_item_price in damaged_item_prices_sorted:
                manufacturers = self.inventory.get_manufacturer_by_itemprice(damaged_item_price)
                for manufacturer in manufacturers:
                    if manufacturer.damaged_indicator == "damaged":
                        writer.writerow(
                        [
                            manufacturer.item_id,
                            manufacturer.manufacturer_name,
                            manufacturer.item_type,
                            manufacturer.item_price,
                            manufacturer.service_date
                        ]
                    )