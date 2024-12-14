from abc import ABC, abstractmethod

from ddd.domain.orders.models import (
    OrderID,
    Order,
)


class OrderRepository(ABC):
    @abstractmethod
    def next_id(self) -> OrderID:
        ...

    @abstractmethod
    def save(self, order: Order):
        pass

    @abstractmethod
    def get_by_id(self, order_id: OrderID):
        pass