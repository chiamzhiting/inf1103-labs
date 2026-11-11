from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0, supplier)
antivirus = DigitalProduct("D001", "Antivirus License", 39.90, 200, 350, supplier)

print("--- Before del supplier ---")
laptop.get_supplier().display_information()
antivirus.get_supplier().display_information()

del supplier   # PREDICT FIRST: what happens to the products' supplier info now?

print("\n--- After del supplier ---")
laptop.get_supplier().display_information()
antivirus.get_supplier().display_information()

print("\n--- Same Supplier object shared by both products? ---")
print(laptop.get_supplier() is antivirus.get_supplier())