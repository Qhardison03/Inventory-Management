# Inventory-Management
This project is designed to build a program that will handle the inventory of an electronics store. This project is coded in Python, using functions, classes, dictionaries, I/O methods, and csv files. 

# Getting Started 
For this project to run locally, make sure you have the following software: 
  - Python (lastest version) 
  - Microsoft VS Code or similar editor 
  - The following csv files:
      - ManufacturerList.csv
      - PriceList.csv
      - ServiceDatesList.csv

This electronics store Inventory Management project was developed and designed in two parts: 

  # Part One: Required Output
            INPUT: 
      ManufacturerList.csv 
      PriceList.csv
      ServiceDatesList.csv
      
         DESIRED OUTPUT:
    - FullInventory.csv --> Items will be listed by row with all their information and sorted alphabetically by manufacturer.
    - Item Type Inventory List (i.e: LaptopInventory.csv) --> File for each item type, with each row containing thier item ID, manufacturer's name, service date, and whether or not it is damaged, and sorted by item ID number.
    - DamagedInventory.csv --> All items that are damaged will be listed and sorted in the order of most expensive to least expensive. 
    
  # Part Two: Interactive Inventory Query Capabilities
    Using the code from Part One:
    - Program will query an item from the user by asking the user for a manufacturer and item type.
    - Program will either: 
      A. Print a message saying "No such item in inventory" if either the manufacturer or item type is not in the inventory, more than one of either type is submitted, or the combination is not in the inventory. 
      B. Print a message saying "Your item is:" with the item ID, manufacturer's name, item type, and item price. If there are more than one item, it will display the most expensive item.
        - Program will also:
          B1. Print a message saying "You may, also, consider:" with information about the same item type from another manufacturer whose price is close to the outputted item.
    - Program will allow user to quit and end the program by pressing 'q'.
