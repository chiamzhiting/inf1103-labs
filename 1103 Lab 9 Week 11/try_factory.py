from supplier import Supplier
from product_factory import ProductFactory

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")

laptop = ProductFactory.create("physical", "P001", "Laptop", 1200.0, 15, supplier, 2.0)
ebook = ProductFactory.create("digital", "D001", "E-book", 9.9, 100, supplier, 5.0)
print(type(laptop).__name__, type(ebook).__name__)
print(laptop.get_fulfilment_info())
print(ebook.get_fulfilment_info())

print("--- unknown type ---")
ProductFactory.create("service", "S001", "Installation", 30.0, 5, supplier)