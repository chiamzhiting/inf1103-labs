from abc import ABC, abstractmethod

from supplier import Supplier


class Product(ABC):
    """Abstract base class representing and managing a single product.

    Every product is either physical or digital, so Product itself can
    never be instantiated directly.

    Association: a Product refers to one Supplier, but does not own it.
    """

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier):
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    # Read-only accessors so other code can see the data without changing it directly
    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity: int) -> bool:
        """Set the stock to a new quantity. Returns False if the value is invalid."""
        if quantity < 0:
            return False
        self.__stock = quantity
        return True

    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
        self.__supplier.display_information()

    def to_dict(self) -> dict:
        """Convert to a plain dict, used by main when saving to JSON."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict(),
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return a message describing how this product is fulfilled.

        No implementation here: every subclass must provide its own.
        """
        pass