from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped

for weight in (1, 3.5, 10):
    item = PhysicalProduct("T", "Test", 1.0, 1, weight)
    print(weight, "kg ->", item.calculate_shipping_cost())

os_lic = DigitalProduct("D1", "Operating System", 99.0, 100, 4500)
print("Digital can be shipped?", isinstance(os_lic, CanBeShipped))