from abc import ABC, abstractmethod

from ordering.domain.orders.model import (
    Order,
    OrderID,
)


class OrderRepository(ABC):
    @abstractmethod
    def next_id(self) -> OrderID:
        ...

    @abstractmethod
    def get_by_id(self, order_id: OrderID):
        pass

    @abstractmethod
    def save(self, order: Order):
        pass