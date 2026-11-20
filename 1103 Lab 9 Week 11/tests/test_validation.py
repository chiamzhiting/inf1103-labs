import pytest

from product_factory import ProductFactory
from order_line import OrderLine


def test_price_zero_rejected(supplier):
    with pytest.raises(ValueError, match="Price must be greater than zero"):
        ProductFactory.create("physical", "P1", "X", 0, 5, supplier, 1.0)


def test_negative_price_rejected(supplier):
    with pytest.raises(ValueError, match="Price must be greater than zero"):
        ProductFactory.create("digital", "D1", "X", -5, 5, supplier, 1.0)


def test_negative_stock_rejected_for_both_subclasses(supplier):
    # LSP: DigitalProduct cannot skip the rule that Product sets.
    with pytest.raises(ValueError, match="cannot be negative"):
        ProductFactory.create("physical", "P1", "X", 10.0, -1, supplier, 1.0)
    with pytest.raises(ValueError, match="cannot be negative"):
        ProductFactory.create("digital", "D1", "X", 10.0, -1, supplier, 1.0)


def test_zero_stock_is_allowed(supplier):
    product = ProductFactory.create("physical", "P1", "X", 10.0, 0, supplier, 1.0)
    assert product.get_stock() == 0


def test_order_line_quantity_zero_rejected(supplier):
    product = ProductFactory.create("physical", "P1", "X", 10.0, 5, supplier, 1.0)
    with pytest.raises(ValueError, match="Quantity must be greater than zero"):
        OrderLine(product, 0)


def test_order_line_negative_quantity_rejected(supplier):
    product = ProductFactory.create("physical", "P1", "X", 10.0, 5, supplier, 1.0)
    with pytest.raises(ValueError):
        OrderLine(product, -2)