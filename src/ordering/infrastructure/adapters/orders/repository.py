import uuid

from ordering.domain.orders.model import (
    Order,
    OrderID,
)
from ordering.domain.orders.repository import OrderRepository

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def next_id(self) -> OrderID:
        return OrderID(uuid.uuid4())

    def save(self, order):
        self.orders[order.id] = order

    def get_by_id(self, order_id: OrderID) -> Order:
        order = self.orders.get(order_id)
        if not order:
            raise ValueError(f"Order {order_id} does not exists")
        return order