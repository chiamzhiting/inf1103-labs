from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped

guitar = PhysicalProduct("P1", "Guitar", 499.0, 5, 3.5)
os_lic = DigitalProduct("D1", "Operating System", 99.0, 100, 4500)

print("--- display_information ---")
guitar.display_information()
os_lic.display_information()

print("--- get_fulfilment_info ---")
print(guitar.get_fulfilment_info())
print(os_lic.get_fulfilment_info())

print("--- shipping costs ---")
for weight in (1, 3.5, 10):
    print(weight, "kg ->", PhysicalProduct("T", "Test", 1.0, 1, weight).calculate_shipping_cost())
print("Digital can be shipped?", isinstance(os_lic, CanBeShipped))

print("--- abstract Product ---")
product = Product("X", "Test", 1.0, 1)