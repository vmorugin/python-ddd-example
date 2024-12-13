from ddd.domain.orders.models import Order
from ddd.domain.orders.repositories import OrderRepository

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def save(self, order):
        self.orders[order.id] = order

    def get_by_id(self, order_id: int) -> Order:
        order = self.orders.get(order_id)
        if not order:
            raise ValueError(f"Order {order_id} does not exists")
        return order