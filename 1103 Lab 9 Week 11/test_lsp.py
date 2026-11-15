from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    """Works with ANY Product. It never asks which subclass it received."""
    product.display_information()
    print(product.get_fulfilment_info())


def check_update_stock_contract(product: Product) -> None:
    """The expectation Product sets for update_stock(): valid values are
    accepted and returned as True; negative values are rejected (False)
    and leave the stock unchanged."""
    original = product.get_stock()
    assert product.update_stock(original + 10) is True
    assert product.get_stock() == original + 10
    assert product.update_stock(-1) is False
    assert product.get_stock() == original + 10   # unchanged by the bad value
    print(f"   {product.get_name()}: update_stock keeps the Product contract")


supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0, supplier)
antivirus = DigitalProduct("D001", "Antivirus License", 39.90, 200, 350, supplier)

print("=== LSP: the same function with both product types ===")
show_product_details(laptop)
print()
show_product_details(antivirus)

print("\n=== LSP: both subclasses added to one Inventory ===")
inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(antivirus)
inventory.display_all()

print("\n=== LSP: the update_stock() expectation holds for both ===")
for product in inventory.get_products():
    check_update_stock_contract(product)