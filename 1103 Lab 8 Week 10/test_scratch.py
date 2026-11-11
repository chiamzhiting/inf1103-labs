from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

# ---------- Section 2: Association ----------
print("=== ASSOCIATION: Supplier and Product ===")
supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0, supplier)
antivirus = DigitalProduct("D001", "Antivirus License", 39.90, 200, 350, supplier)

print("--- Before del supplier ---")
laptop.get_supplier().display_information()
antivirus.get_supplier().display_information()

del supplier   # PREDICT FIRST: what happens to the products' supplier info now?

print("--- After del supplier ---")
laptop.get_supplier().display_information()
antivirus.get_supplier().display_information()

print("Same Supplier object shared by both products?",
      laptop.get_supplier() is antivirus.get_supplier())

# ---------- Section 3: Aggregation ----------
print("\n=== AGGREGATION: Inventory and Product ===")
mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, 0.1, laptop.get_supplier())
print("Mouse created BEFORE any inventory exists:", mouse.get_name())

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(mouse)
inventory_a.add_product(antivirus)
print("Inventory A has the mouse?", inventory_a.find_product("P002") is mouse)

# PREDICT FIRST: after removing the mouse from Inventory A, does the Product still work?
inventory_a.remove_product("P002")
print("Inventory A still has the mouse?", inventory_a.find_product("P002") is not None)
print("Mouse still usable after removal:")
mouse.display_information()

inventory_b.add_product(mouse)
print("Same mouse object now in Inventory B?", inventory_b.find_product("P002") is mouse)

print("Removing a product that does not exist returns:", inventory_a.remove_product("X999"))
print("Finding a product that does not exist returns:", inventory_a.find_product("X999"))

# Empty an inventory: the products are not destroyed.
inventory_a.remove_product("D001")
print("Inventory A is now empty, but antivirus still exists:", antivirus.get_name())