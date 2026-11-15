from discount_strategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float):
        self.__threshold: float = threshold
        self.__amount: float = amount

    def apply(self, total: float) -> float:
        return total - self.__amount if total >= self.__threshold else total