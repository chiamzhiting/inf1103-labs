from discount_strategy import DiscountStrategy


class StudentDiscount(DiscountStrategy):
    """5% off for students."""

    def apply(self, total: float) -> float:
        return total * 0.95