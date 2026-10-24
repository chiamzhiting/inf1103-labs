6
import json
import os

from product import Product
from inventory import Inventory

DATA_FILE = "data/inventory.json"


# ---------- File handling ----------
def load_inventory(filename=DATA_FILE):
    inventory = Inventory()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for item in json.load(f):
                inventory.add_product(
                    Product(item["id"], item["name"], item["price"], item["stock"])
                )
    else:
        # fallback starter products
        inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
        inventory.add_product(Product("P002", "Mouse", 25.50, 40))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 25))
    return inventory


def save_inventory(inventory, filename=DATA_FILE):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data = [product.to_dict() for product in inventory.get_products()]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# ---------- Menu ----------
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
            inventory.display_all()

        elif choice == "2":
            pid = input("Product ID: ")
            if inventory.search_product(pid):
                print("A product with that ID already exists.")
                continue
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
            except ValueError:
                print("Invalid number entered. Product not added.")
                continue
            inventory.add_product(Product(pid, name, price, stock))
            print("Product added successfully!")

        elif choice == "3":
            pid = input("Enter Product ID: ")
            product = inventory.search_product(pid)
            if product is None:
                print("Product not found.")
                continue
            try:
                new_stock = int(input("New Stock Quantity: "))
            except ValueError:
                print("Invalid number entered.")
                continue
            if product.update_stock(new_stock):
                print("Stock updated successfully!")
            else:
                print("Stock cannot be negative.")

        elif choice == "4":
            pid = input("Enter Product ID: ")
            product = inventory.search_product(pid)
            if product:
                print("\nProduct Found")
                print("-" * 48)
                product.display_information()
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


if __name__ == "__main__":
    menu()