from abc import ABC, abstractmethod

from ddd.domain.orders.models import (
    Order,
    Product,
    Customer,
    OrderID,
)


class OrderServiceInterface(ABC):
    @abstractmethod
    def get_order(self, order_id: OrderID) -> Order:
        ...

    @abstractmethod
    def create_order(self, customer: Customer, products: list[Product]) -> Order:
        pass

    @abstractmethod
    def apply_discount(self, order_id: OrderID, discount_percentage: float):
        pass