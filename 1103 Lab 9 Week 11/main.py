import json
import os

from inventory import Inventory
from can_be_shipped import CanBeShipped
from product import Product
from product_factory import ProductFactory
from supplier import Supplier

DATA_FILE = "data/inventory.json"

# Used for old saved records (from Lab 7) that have no supplier information.
DEFAULT_SUPPLIER = {"id": "S000", "name": "Unknown Supplier", "contact_email": "n/a"}


# ---------- Suppliers ----------
def get_or_create_supplier(suppliers: dict[str, Supplier], supplier_id: str,
                           name: str, contact_email: str) -> Supplier:
    """Reuse an existing Supplier object if we already have one with this ID.

    This is why many products can share ONE Supplier object (association).
    """
    if supplier_id not in suppliers:
        suppliers[supplier_id] = Supplier(supplier_id, name, contact_email)
    return suppliers[supplier_id]


# ---------- File handling ----------
def create_product_from_dict(item: dict, suppliers: dict[str, Supplier]) -> Product:
    """Build the correct Product subclass from a saved record using the factory."""
    data = item.get("supplier", DEFAULT_SUPPLIER)
    supplier = get_or_create_supplier(suppliers, data["id"], data["name"],
                                      data["contact_email"])
    extra = item.get("weight", item.get("download_size", 0.0))
    return ProductFactory.create(item.get("type"), item["id"], item["name"],
                                 item["price"], item["stock"], supplier, extra)


def load_inventory(filename: str = DATA_FILE) -> tuple[Inventory, dict[str, Supplier]]:
    inventory = Inventory()
    suppliers: dict[str, Supplier] = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for item in json.load(f):
                try:
                    product = create_product_from_dict(item, suppliers)
                except (KeyError, ValueError) as error:
                    print(f"Skipped a saved record ({error}).")
                    continue
                if inventory.find_product(product.get_product_id()):
                    print(f"Skipped duplicate product ID {product.get_product_id()}.")
                    continue
                inventory.add_product(product)
    else:
        # fallback starter products (all from one shared Supplier object)
        supplier = get_or_create_supplier(suppliers, "S001", "TechSource Pte Ltd",
                                          "sales@techsource.com")
        inventory.add_product(ProductFactory.create("physical", "P001", "Laptop", 1200.00, 15, supplier, 2.0))
        inventory.add_product(ProductFactory.create("physical", "P002", "Mouse", 25.50, 40, supplier, 0.1))
        inventory.add_product(ProductFactory.create("physical", "P003", "Keyboard", 45.00, 25, supplier, 0.8))
        inventory.add_product(ProductFactory.create("digital", "D001", "Antivirus License", 39.90, 200, supplier, 350))
    return inventory, suppliers


def save_inventory(inventory: Inventory, filename: str = DATA_FILE) -> None:
    folder = os.path.dirname(filename)
    if folder:
        os.makedirs(folder, exist_ok=True)
    data = [product.to_dict() for product in inventory.get_products()]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# ---------- Menu ----------
def menu() -> None:
    inventory, suppliers = load_inventory()
    print("Inventory loaded successfully.")

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Remove Product")
        print("6. Save Inventory")
        print("7. Exit")
        print("----------------------------")

        choice = input("Enter option: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            print("Product type: 1. Physical  2. Digital")
            product_type = input("Choose type: ")
            if product_type not in ("1", "2"):
                print("Invalid product type. Product not added.")
                continue
            pid = input("Product ID: ")
            if inventory.find_product(pid):
                print("A product with that ID already exists.")
                continue
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
                if product_type == "1":
                    weight = float(input("Weight (kg): "))
                else:
                    download_size = float(input("Download Size (MB): "))
            except ValueError:
                print("Invalid number entered. Product not added.")
                continue
            extra = weight if product_type == "1" else download_size
            if price < 0 or stock < 0 or extra < 0:
                print("Values cannot be negative. Product not added.")
                continue

            # The Supplier is created independently, then handed to the Product.
            supplier_id = input("Supplier ID: ")
            supplier = suppliers.get(supplier_id)
            if supplier is None:
                supplier_name = input("New supplier name: ")
                supplier_email = input("Supplier contact email: ")
                supplier = get_or_create_supplier(suppliers, supplier_id,
                                                  supplier_name, supplier_email)

            type_name = "physical" if product_type == "1" else "digital"
            try:
                product = ProductFactory.create(type_name, pid, name, price,
                                                stock, supplier, extra)
            except ValueError as error:
                print(f"Product not added: {error}")
                continue
            inventory.add_product(product)
            print("Product added successfully!")

        elif choice == "3":
            pid = input("Enter Product ID: ")
            product = inventory.find_product(pid)
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
            product = inventory.find_product(pid)
            if product:
                print("\nProduct Found")
                print("-" * 48)
                product.display_information()
                print(f"   Fulfilment: {product.get_fulfilment_info()}")
                if isinstance(product, CanBeShipped):
                    print(f"   Shipping cost: ${product.calculate_shipping_cost():.2f}")
                print("-" * 48)
            else:
                print("Product not found.")

        elif choice == "5":
            pid = input("Enter Product ID to remove: ")
            if inventory.remove_product(pid):
                print("Product removed from the inventory.")
            else:
                print("Product not found.")

        elif choice == "6":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully.")

        elif choice == "7":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()