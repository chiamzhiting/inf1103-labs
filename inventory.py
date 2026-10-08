import json
import os

#inventory = [
    #{"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    #{"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    #{"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
#]

def load_inventory(filename="inventory.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_inventory(inventory, filename="inventory.json"):
    with open(filename, "w") as f:
        json.dump(inventory, f, indent=4)

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

def menu():
    inventory = load_inventory()
    print("Inventory loaded successfully.")

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        choice = input("Enter option: ")

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            pid = input("Product ID: ")
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
            add_product(inventory, {"id": pid, "name": name, "price": price, "stock": stock})
            print("Product added successfully!")
        elif choice == "3":
            pid = input("Enter Product ID: ")
            new_stock = int(input("New Stock Quantity: "))
            if update_stock(inventory, pid, new_stock):
                print("Stock updated successfully!")
            else:
                print("Product not found.")
        elif choice == "4":
            pid = input("Enter Product ID: ")
            product = search_product(inventory, pid)
            if product:
                print("\nProduct Found")
                print("-" * 48)
                print(f"ID: {product['id']}\nName: {product['name']}\nPrice: ${product['price']:.2f}\nStock: {product['stock']}")
                print("-" * 48)
            else:
                print("Product not found.")
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            break
        else:
            print("Invalid option. Try again.")

