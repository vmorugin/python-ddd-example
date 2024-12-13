from dataclasses import dataclass

@dataclass(kw_only=True, frozen=True)
class Customer:
    id: int

@dataclass(kw_only=True, frozen=True)
class Product:
    id: int
    name: str
    price: float

@dataclass(kw_only=True)
class Order:
    id: int
    customer: Customer
    products: list[Product]
    total: float = 0.0

    def calculate_total(self):
        self.total = sum(product.price for product in self.products)

    def apply_discount(self, discount_percentage: float):
        discount = self.total * (discount_percentage / 100)
        self.total -= discount