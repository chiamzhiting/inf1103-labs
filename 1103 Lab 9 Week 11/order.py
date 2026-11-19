from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    """A customer order made up of OrderLine objects.

    Composition: the Order creates and manages its own OrderLines. Callers
    pass in a Product and a quantity, never a ready-made OrderLine.
    """

    def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = NoDiscount() if discount is None else discount

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        """Return a copy of the list so callers cannot add or remove lines directly."""
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Create an OrderLine inside this Order and add it."""
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        """Remove the line for this product. Returns False if there is none.

        The OrderLine is discarded with the Order's data; the Product is untouched.
        """
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                return True
        return False
    
    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def calculate_total(self) -> float:
        """Total after the discount strategy has been applied to the line subtotals."""
        subtotal = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(subtotal)

    def display_information(self) -> None:
        print(f"Order {self.__order_id}")
        for order_line in self.__order_lines:
            order_line.display_information()
        print(f"   Total: ${self.calculate_total():.2f}")