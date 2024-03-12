# Quentin Hardison

import ProjectInput_p2
import ProjectOutput_p2


# Creates Manufacturer class that includes:
# item id, manufacturer's name, item type, item price, service date, and damaged indicator

class Manufacturer:
    """
    Creates Manufacturer class that includes:
        item id, manufacturer's name, item type, item price, service date, and damaged indicator
    """
    def __init__(self, item_id, manufacturer_name, item_type, item_price, service_date, damaged_indicator):
        self.item_id = item_id
        self.manufacturer_name = manufacturer_name
        self.item_type = item_type
        self.item_price = item_price
        self.service_date = service_date
        self.damaged_indicator = damaged_indicator

# Creates a class called Inventory containing a dictionary of manufacturers
class Inventory:
    def __init__(self):
        self.manufacturers = {}

# Function created to add a manufacturer
    def add_manufacturer(self, manufacturer):
        self.manufacturers[manufacturer.item_id] = manufacturer

# Function created to get a manufacturer
    def get_manufacturer(self, item_id):
        return self.manufacturers[item_id]

    def get_manufacturer_by_name(self, manufacturer_name):
        manufacturer_by_name = []
        for item_id in self.manufacturers:
            manufacturer = self.manufacturers[item_id]
            if manufacturer.manufacturer_name == manufacturer_name:
                manufacturer_by_name.append(manufacturer)
        return manufacturer_by_name

    def get_manufacturer_by_itemtype(self, item_type):
        manufacturer_by_type = []
        for item_id in self.manufacturers:
            manufacturer = self.manufacturers[item_id]
            if manufacturer.item_type == item_type:
                manufacturer_by_type.append(manufacturer)
        return manufacturer_by_type

    def get_all_manufacturers(self):
        all_manufacturers = []
        for item_id in self.manufacturers:
            manufacturer = self.manufacturers[item_id]
            all_manufacturers.append(manufacturer)
        return all_manufacturers

    def get_manufacturer_by_itemprice(self, item_price):
        manufacturers_by_price = []
        for item_id in self.manufacturers:
            manufacturer = self.manufacturers[item_id]
            if manufacturer.item_price == item_price:
                manufacturers_by_price.append(manufacturer)
        return manufacturers_by_price

    def get_manufacturer_by_servicedate(self, service_date):
        manufacturers_by_date = []
        for item_id in self.manufacturers:
            manufacturer = self.manufacturers[item_id]
            if manufacturer.service_date == service_date:
                manufacturers_by_date.append(manufacturer)
        return manufacturers_by_date

    def get_any_damaged_indicators(self, damaged_indicator):
        manufacturers_by_damaged_indicator = []
        for item_id in self.manufacturers:
            manufacturer = self.manufacturers[item_id]
            if manufacturer.damaged_indicator == damaged_indicator:
                manufacturers_by_damaged_indicator.append(manufacturer)
        return manufacturers_by_damaged_indicator


if __name__ == "__main__":
    # Creates Inventory Class
    inventory = Inventory()

    # Reads from input files and store values into inventory instance
    inventoryInput = ProjectInput_p2.InventoryInput(inventory)
    inventoryInput.read_from_manufacturer_list("ManufacturerList.csv")
    inventoryInput.read_from_price_list("PriceList.csv")
    inventoryInput.read_from_service_dates_list("ServiceDatesList.csv")

    # Gets the stored values from inventory instance, and writes into csv
    processedInventoryReport = ProjectOutput_p2.ProcessedInventoryReport(inventory)
    processedInventoryReport.write_full_inventory_report("FullInventory.csv")
    processedInventoryReport.write_item_type_inventory_list_report()
    processedInventoryReport.write_past_service_date_inventory("PastServiceDateInventory.csv")
    processedInventoryReport.write_damaged_inventory_report("DamagedInventory.csv")

    # Part 2: Interactive Inventory Query Capability
    from datetime import datetime
    today = datetime.now()

    cont = True

    # Keep on query the user until user enter "q"
    while cont:
        print()
        # Query the user of an item by asking for manufacturer and item type
        user_input = input("Please input manufacturer name and item type, separated by a space. e.g. Apple laptop: ")
        print()

        # Terminate the loop if user enter "q"
        if user_input == "q":
            break

        # Convert string user input into list of words
        list_of_words = user_input.split()

        # Initialize boolean variable
        manufacturer_exist = False
        item_exist = False

        # Iterate through all the words in the list
        # This loop is used to extract keyword in input: "nice samsung phone" -> samsung & phone
        for word in list_of_words:
            # Clean word
            # Manufacturer name in dictionary is always start as upper case, follow by all lower cases
            manufacturer_name = word[0].upper() + word[1:].lower()
            # item name in dictionary is always lower cases
            item_name = word.lower()

            # Check if manufacturer and item type exists in inventory
            found_manufacturer_name = len(inventory.get_manufacturer_by_name(manufacturer_name)) > 0
            found_item_type = len(inventory.get_manufacturer_by_itemtype(item_name)) > 0

            # If more that one of manufacturer name or item type is submitted (e.g. apple samsung phone), 
            # terminate the loop and print no such item
            if manufacturer_exist is True and found_manufacturer_name:
                manufacturer_exist = False
                break

            if item_exist is True and found_item_type:
                item_exist = False
                break
            
            # Check if manufacturer name and item type is found in inventory
            if found_manufacturer_name:
                manufacturer_name_found = manufacturer_name
                manufacturer_exist = True
            if found_item_type:
                item_type_found = item_name
                item_exist = True
        
        # Take the extracted keywords to run search
        if manufacturer_exist and item_exist:
            # Initialize variable for comparison for item price, with objective: "provide the most expensive item"
            most_expensive_item_id = None
            highest_price = 0
            manufacturers = inventory.get_manufacturer_by_name(manufacturer_name_found)

            # Iterate through all the manufacturer with same name
            for manufacturer in manufacturers:
                # Check service date
                is_expired = False
                service_date_formatted = datetime.strptime(manufacturer.service_date, "%m/%d/%Y")
                if service_date_formatted < today:
                    is_expired = True

                # Check if same item type, past their service date, or damaged
                # (Do not provide items that are past their service date or damaged)
                if manufacturer.item_type == item_type_found and len(manufacturer.damaged_indicator)==0 and not is_expired:
                    # compare price
                    if float(manufacturer.item_price) > highest_price:
                        # Overwrite the current most expensive item and highest price
                        most_expensive_item_id = manufacturer.item_id
                        highest_price = float(manufacturer.item_price)

            # Check if all the requirements met: No expired item, no damaged item, item type found, manufacturer matched
            if most_expensive_item_id is not None:
                final_manufacturer = inventory.get_manufacturer(most_expensive_item_id)
                print(f"Your item is: {final_manufacturer.item_id}, {final_manufacturer.manufacturer_name}, {final_manufacturer.item_type}, {final_manufacturer.item_price}.")

                # 1a(iii): You may, also, consider 
                # Get all manufacturer with same item type
                other_manufacturers_with_same_item_type = inventory.get_manufacturer_by_itemtype(item_type_found)
                # Get the manufacturer with closest price
                closest_manufacturer = None
                cloest_price_diff = 999999
                # Iterate through all the manufacturer with same item type
                for same_item_manufacturer in other_manufacturers_with_same_item_type:
                    # Take only other manufacturer
                    if same_item_manufacturer.manufacturer_name != final_manufacturer.manufacturer_name:
                        # Compute the difference with the current price, and find the closest
                        diff = abs(float(same_item_manufacturer.item_price) - float(final_manufacturer.item_price))
                        if diff < cloest_price_diff:
                            closest_manufacturer = same_item_manufacturer
                            cloest_price_diff = diff

                if closest_manufacturer is not None:
                    print(f"You may, also, consider: {closest_manufacturer.item_id}, {closest_manufacturer.manufacturer_name}, {closest_manufacturer.item_type}, {closest_manufacturer.item_price}.")

        # At the end of the loop, if either the manufacturer or the item type are not in the inventory
        else:
            print("No such item in inventory")
