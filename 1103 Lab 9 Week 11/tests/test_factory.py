import pytest

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory


def test_factory_creates_physical_product(supplier):
    product = ProductFactory.create("physical", "P1", "Laptop", 1200.0, 5, supplier, 2.0)
    assert isinstance(product, PhysicalProduct)
    assert isinstance(product, Product)
    assert product.get_weight() == 2.0


def test_factory_creates_digital_product(supplier):
    product = ProductFactory.create("digital", "D1", "E-book", 9.9, 100, supplier, 5.0)
    assert isinstance(product, DigitalProduct)
    assert product.get_download_size() == 5.0


def test_unknown_product_type_raises_value_error(supplier):
    with pytest.raises(ValueError, match="Unknown product type: service"):
        ProductFactory.create("service", "S1", "Installation", 30.0, 5, supplier)


def test_factory_products_share_the_supplier(supplier):
    a = ProductFactory.create("physical", "P1", "A", 10.0, 1, supplier, 1.0)
    b = ProductFactory.create("digital", "D1", "B", 10.0, 1, supplier, 1.0)
    assert a.get_supplier() is b.get_supplier()