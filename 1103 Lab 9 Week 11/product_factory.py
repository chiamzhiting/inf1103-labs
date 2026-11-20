from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class ProductFactory:
    """Centralises product creation. The rest of the program only asks for a Product."""

    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock: int, supplier: Supplier, extra: float = 0.0) -> Product:
        """extra = weight (kg) for physical products, download size (MB) for digital."""
        if product_type == PhysicalProduct.TYPE:
            return PhysicalProduct(product_id, name, price, stock, extra, supplier)
        elif product_type == DigitalProduct.TYPE:
            return DigitalProduct(product_id, name, price, stock, extra, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")