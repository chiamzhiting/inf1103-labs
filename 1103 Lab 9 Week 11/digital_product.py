from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    """A downloadable product. It is not shipped, so it does not implement CanBeShipped."""

    TYPE = "digital"

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"   Type: Digital | Download size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "Digital product: delivered digitally through a download link."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = self.TYPE
        data["download_size"] = self.__download_size
        return data