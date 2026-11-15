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

# ---------- Section 4: Composition ----------
from order import Order

print("\n=== COMPOSITION: Order and OrderLine ===")
keyboard = PhysicalProduct("P003", "Keyboard", 45.00, 25, 0.8, laptop.get_supplier())

order_1 = Order("O001")
order_1.add_order_line(laptop, 1)
order_1.add_order_line(mouse, 2)
order_1.add_order_line(antivirus, 3)
order_1.display_information()
print("Order 1 total is correct (1200 + 2*25.50 + 3*39.90 = 1370.70):",
      round(order_1.calculate_total(), 2) == 1370.70)

# PREDICT FIRST: the same Product goes into a second Order.
# How many OrderLine objects and how many Product objects will exist?
order_2 = Order("O002")
order_2.add_order_line(laptop, 5)
order_2.add_order_line(keyboard, 1)

line_1 = order_1.get_order_lines()[0]
line_2 = order_2.get_order_lines()[0]
print("\nSame OrderLine object in both orders?", line_1 is line_2)
print("Same Product object in both lines?   ", line_1.get_product() is line_2.get_product())
print("Order 1 line id:", id(line_1), "| Order 2 line id:", id(line_2))
print("Laptop id via line 1:", id(line_1.get_product()),
      "| via line 2:", id(line_2.get_product()))

print("\nRemoving the mouse line from Order 1 through the Order:")
print("Removed?", order_1.remove_order_line("P002"))
order_1.display_information()
print("The mouse Product still exists:", mouse.get_name())

print("\nOrder 2 is unaffected:")
order_2.display_information()