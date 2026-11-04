from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    """A tangible product that is stored and shipped.

    Single inheritance from Product, plus the CanBeShipped interface.
    """

    TYPE = "physical"
    BASE_SHIPPING_COST = 5.00   # flat handling fee ($)
    COST_PER_KG = 2.00          # added for every kilogram ($)

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"   Type: Physical | Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "Physical product: requires packing and physical shipping."

    def calculate_shipping_cost(self):
        """Simple rule: flat handling fee plus a rate per kilogram."""
        return self.BASE_SHIPPING_COST + self.COST_PER_KG * self.__weight

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["weight"] = self.__weight
        return data