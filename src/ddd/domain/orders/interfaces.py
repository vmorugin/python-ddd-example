from abc import ABC, abstractmethod

from ddd.domain.orders.models import (
    Order,
    Product,
    Customer,
)


class OrderServiceInterface(ABC):
    @abstractmethod
    def get_order(self, order_id: int) -> Order:
        ...

    @abstractmethod
    def create_order(self, order_id: int, customer: Customer, products: list[Product]) -> Order:
        pass

    @abstractmethod
    def apply_discount(self, order_id: int, discount_percentage: float):
        pass