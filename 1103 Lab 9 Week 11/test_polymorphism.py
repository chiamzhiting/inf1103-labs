from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")

inventory = Inventory()
inventory.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0, supplier))
inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, 0.1, supplier))
inventory.add_product(DigitalProduct("D001", "Antivirus License", 39.90, 200, 350, supplier))
inventory.add_product(DigitalProduct("D002", "Photo Editor", 59.00, 80, 520, supplier))

# PREDICT FIRST: write down what get_fulfilment_info() will print for each product
# BEFORE running this file.

print("=== One loop over the Product collection (no isinstance, no separate loops) ===")
for product in inventory.get_products():
    product.display_information()
    print(f"   Fulfilment: {product.get_fulfilment_info()}")
    print()