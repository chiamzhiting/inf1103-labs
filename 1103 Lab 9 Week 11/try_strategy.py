from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
item = PhysicalProduct("P001", "Test Item", 50.00, 20, 1.0, supplier)

order = Order("O001", BulkDiscount(200, 20))
order.add_order_line(item, 5)          # 5 x 50 = 250
print("Bulk:", order.calculate_total())

order.set_discount(PercentageDiscount(10))
print("Percentage:", order.calculate_total())

print("Default:", Order("O002").calculate_total())