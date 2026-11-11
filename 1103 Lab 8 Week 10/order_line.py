from product import Product


class OrderLine:
    """One product and the quantity requested of it within a single Order.

    Composition: an OrderLine is created and managed by its Order (see
    Order.add_order_line). It is not meant to exist on its own or be moved
    to another Order.

    Association: an OrderLine refers to a Product but does not own it.
    """

    def __init__(self, product: Product, quantity: int):
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(f"   {self.__product.get_name()} x {self.__quantity} "
              f"@ ${self.__product.get_price():.2f} = ${self.calculate_subtotal():.2f}")