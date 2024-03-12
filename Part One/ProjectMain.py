import ProjectInput
import ProjectOutput


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
    inventoryInput = ProjectInput.InventoryInput(inventory)
    inventoryInput.read_from_manufacturer_list("ManufacturerList.csv")
    inventoryInput.read_from_price_list("PriceList.csv")
    inventoryInput.read_from_service_dates_list("ServiceDatesList.csv")

    # Gets the stored values from inventory instance, and writes into csv
    processedInventoryReport = ProjectOutput.ProcessedInventoryReport(inventory)
    processedInventoryReport.write_full_inventory_report("FullInventory.csv")
    processedInventoryReport.write_item_type_inventory_list_report()
    processedInventoryReport.write_past_service_date_inventory("PastServiceDateInventory.csv")
    processedInventoryReport.write_damaged_inventory_report("DamagedInventory.csv")