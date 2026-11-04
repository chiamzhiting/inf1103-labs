from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P1", "Guitar", 499.0, 5, 3.5)
os_lic = DigitalProduct("D1", "Operating System", 99.0, 100, 4500)

guitar.display_information()
os_lic.display_information()