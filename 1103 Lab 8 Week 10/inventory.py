from product import Product


class Inventory:
    """Manages a collection of Product objects.

    Aggregation: an Inventory holds references to Products, but it does not
    create them or control their lifecycle. Removing a Product from the
    Inventory only removes the reference; the Product itself still exists.
    """

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """Add an existing Product object to this inventory."""
        self.__products.append(product)

    def remove_product(self, product_id: str) -> bool:
        """Remove the matching Product reference. Returns False if it was not found.

        The Product object itself is NOT destroyed or changed.
        """
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        """Return the matching Product, or None if not found."""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-" * 48)
        if not self.__products:
            print("No products found.")
        else:
            for product in self.__products:
                product.display_information()
        print("-" * 48)

    def get_products(self) -> list[Product]:
        """Return a copy of the product list (so callers can't alter the original list)."""
        return list(self.__products)