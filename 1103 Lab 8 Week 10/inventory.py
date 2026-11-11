from product import Product


class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def search_product(self, product_id: str) -> Product | None:
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