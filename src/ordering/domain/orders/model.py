import typing as t
import uuid
from dataclasses import (
    dataclass,
    field,
)
from uuid import UUID

class OrderID:
    def __init__(self, value: str | UUID):
        self._value = str(value)

    @classmethod
    def generate(cls) -> 'OrderID':
        return cls(uuid.uuid4())

    def __hash__(self) -> int:
        return hash(self._value)

    def __eq__(self, other: t.Any):
        return self.__class__ == other.__class__ and self.__hash__() == other.__hash__()


@dataclass(kw_only=True, frozen=True)
class Customer:
    id: str


@dataclass(kw_only=True, frozen=True)
class Product:
    id: str
    name: str
    price: float


@dataclass(kw_only=True)
class Order:
    id: OrderID
    customer: Customer
    products: list[Product] = field(default_factory=list)
    discount: float = 0.0

    def calculate_price(self):
        total = sum(product.price for product in self.products)
        discount = total * (self.discount / 100)
        return total - discount

    def apply_discount(self, discount_percentage: float):
        self.discount = discount_percentage
