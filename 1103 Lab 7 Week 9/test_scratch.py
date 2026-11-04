from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P1", "Guitar", 499.0, 5, 3.5)
os_lic = DigitalProduct("D1", "Operating System", 99.0, 100, 4500)

print(guitar.get_fulfilment_info())
print(os_lic.get_fulfilment_info())

# This should fail, because Product is now abstract
product = Product("X", "Test", 1.0, 1)