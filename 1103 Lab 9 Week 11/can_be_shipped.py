from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface-style contract: any class that signs this can be shipped.

    It holds no attributes and no shipping logic, only the required behaviour.
    """

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Return the cost of shipping this item."""
        pass