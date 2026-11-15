"""Prints the type hints of each class, as evidence for the lab submission."""
from typing import get_type_hints

from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order_line import OrderLine
from order import Order
from can_be_shipped import CanBeShipped

classes = [Supplier, Product, PhysicalProduct, DigitalProduct,
           Inventory, OrderLine, Order, CanBeShipped]

for cls in classes:
    print(f"\n{cls.__name__}")
    for name, member in vars(cls).items():
        if callable(member) and not name.startswith("__") or name == "__init__":
            hints = get_type_hints(member)
            if hints:
                print(f"   {name}: {hints}")