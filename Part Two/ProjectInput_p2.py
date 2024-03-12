# Quentin Hardison

import csv
import ProjectMain_p2


class InventoryInput:
    """
    This class processes the input data and then stores them in Inventory instance
        There are 3 inputs to be read:
            1. ManufacturerList.csv
            2. PriceList.csv
            3. ServiceDatesList.csv
    """
    # Creates InventoryInput class with Inventory as its properties
    def __init__(self, inventory):
        self.inventory = inventory


    def read_from_manufacturer_list(self, filename):
        """
        Function reads all the items from ManufacturerList.csv, store them into Manufacturer Class,
           Then stores the Manufacturer Class in an Inventory instance

        Each row of ManufacturerList contains item ID, manufacturer name, item type, and optionally a damaged indicator
        Parameter:
            filename (str): The name of csv file to be read (e.g. ManufacturerList.csv)
        """
        with open(filename, "r") as manufacturerlist_csvfile:
            # Reads the csv file
            manufacturerlist_reader = csv.reader(manufacturerlist_csvfile)
            # Repeats through each row in ManufacturerList.csv
            for row in manufacturerlist_reader:
                # Item id is at first row
                item_id = row[0]
                # manfacturer's name is at second row
                manufacturer_name =row[1].replace(" ", "")
                # item type is at third row
                item_type = row[2]
                # Sets item price as None (will be added later)
                item_price = None
                # Sets service date as None (will be added later)
                service_date = None
                # damage indicator is at fourth row
                damaged_indicator = row[3]
                
                # Creates a new class for this manufacturer
                manufacturer = ProjectMain_p2.Manufacturer(
                    item_id=item_id,
                    manufacturer_name=manufacturer_name,
                    item_type=item_type,
                    item_price=item_price,
                    service_date=service_date,
                    damaged_indicator=damaged_indicator
                )

                # Add this manufacturer object into Inventory Class
                self.inventory.add_manufacturer(manufacturer)


    def read_from_price_list(self, filename):
        """
        Function reads all the items from PriceList,
            Then overrides the price in Manufacturer Class with the updated price

        Each row of PriceList contains item ID, and item price
        Parameter:
            filename (str): The name of csv file to be read (e.g. PriceList.csv)
        """
        with open(filename, "r") as pricelist_csvfile:
            # Reads the csv file
            pricelist_reader = csv.reader(pricelist_csvfile)
            # Repeats through each row in PriceList.csv
            for row in pricelist_reader:
                # Item id is at first row
                item_id = row[0]
                # Item price is at second row
                item_price = row[1]
                # Retrieves manufacturer by this specific item_id
                manufacturer = self.inventory.get_manufacturer(item_id)
                # Overwrites the item price for this manufacturer from None to new item price
                manufacturer.item_price = item_price


    def read_from_service_dates_list(self, filename):
        """
        Function reads all the items from ServiceDatesList
            Then overrides the service date in Manufacturer Class with the updated date

        Each row of ServiceDatesList contains item ID, and service date.
        Parameter:
            filename (str): The name of csv file to be read (e.g. ServiceDatesList.csv)
        """
        with open(filename, "r") as servicedatelist_csvfile:
            # Reads the csv file
            servicedatelist_reader = csv.reader(servicedatelist_csvfile)
            # Repeats through each row in PriceList.csv
            for row in servicedatelist_reader:
                # Item id is at first row
                item_id = row[0]
                # Service date is at second row
                service_date = row[1]
                # Retrieves manufacturer by this specific item_id
                manufacturer = self.inventory.get_manufacturer(item_id)
                # Overwrites the item price for this manufacturer from None to new item price
                manufacturer.service_date = service_date