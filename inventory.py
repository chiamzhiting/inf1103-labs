inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

def add_product(inventory, product):
    inventory.append(product)

def update_stock(inventory, product_id, new_stock):
    for item in inventory:
        if item["id"] == product_id:
            item["stock"] = new_stock
            return True
    return False

def search_product(inventory, product_id):
    for item in inventory:
        if item["id"] == product_id:
            return item
    return None

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")
    print("-" * 48)

import json
import os

def load_inventory(filename="inventory.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_inventory(inventory, filename="inventory.json"):
    with open(filename, "w") as f:
        json.dump(inventory, f, indent=4)
