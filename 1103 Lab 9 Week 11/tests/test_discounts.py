import inspect

from discount_strategy import DiscountStrategy
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount
from order import Order
from product_factory import ProductFactory


def make_order_of_250(supplier, discount=None):
    item = ProductFactory.create("physical", "P001", "Item", 50.0, 20, supplier, 1.0)
    order = Order("O001", discount)
    order.add_order_line(item, 5)  # 5 x 50 = 250
    return order


def test_no_discount_returns_total_unchanged():
    assert NoDiscount().apply(250) == 250


def test_percentage_discount():
    assert PercentageDiscount(10).apply(250) == 225


def test_bulk_discount_at_or_above_threshold():
    assert BulkDiscount(200, 20).apply(250) == 230
    assert BulkDiscount(200, 20).apply(200) == 180


def test_bulk_discount_below_threshold():
    assert BulkDiscount(200, 20).apply(150) == 150


def test_student_discount():
    assert StudentDiscount().apply(250) == 237.5


def test_order_defaults_to_no_discount(supplier):
    assert make_order_of_250(supplier).calculate_total() == 250


def test_order_totals_through_strategy(supplier):
    order = make_order_of_250(supplier, BulkDiscount(200, 20))
    assert order.calculate_total() == 230


def test_set_discount_changes_strategy(supplier):
    order = make_order_of_250(supplier, BulkDiscount(200, 20))
    order.set_discount(PercentageDiscount(10))
    assert order.calculate_total() == 225


def test_new_strategy_works_without_changing_order(supplier):
    # A brand new strategy defined here, Order is never edited.
    class HalfPrice(DiscountStrategy):
        def apply(self, total: float) -> float:
            return total / 2

    order = make_order_of_250(supplier)
    order.set_discount(HalfPrice())
    assert order.calculate_total() == 125


def test_order_has_no_discount_if_elif_logic():
    source = inspect.getsource(Order.calculate_total)
    assert "if " not in source
    assert "elif" not in source