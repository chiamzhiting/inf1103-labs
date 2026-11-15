from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Contract for any discount. Order only ever calls apply()."""

    @abstractmethod
    def apply(self, total: float) -> float:
        pass