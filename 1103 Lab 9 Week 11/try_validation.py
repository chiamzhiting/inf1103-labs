from supplier import Supplier
from product_factory import ProductFactory
from order import Order

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
good = ProductFactory.create("physical", "P001", "Laptop", 1200.0, 15, supplier, 2.0)

for label, action in [
    ("price 0", lambda: ProductFactory.create("physical", "P2", "X", 0, 5, supplier, 1.0)),
    ("negative price", lambda: ProductFactory.create("digital", "D2", "X", -5, 5, supplier, 1.0)),
    ("negative stock", lambda: ProductFactory.create("physical", "P3", "X", 10, -1, supplier, 1.0)),
    ("quantity 0", lambda: Order("O1").add_order_line(good, 0)),
]:
    try:
        action()
        print(label, "-> accepted (this is wrong!)")
    except ValueError as error:
        print(label, "-> rejected:", error)