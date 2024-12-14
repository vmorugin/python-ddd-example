from ordering.domain.orders.interfaces import OrderServiceInterface
from ordering.domain.orders.repository import OrderRepository
from ordering.domain.orders.model import (
    Order,
    Product,
    Customer,
    OrderID,
)


class OrderService(OrderServiceInterface):
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def get_order(self, order_id: OrderID) -> Order:
        return self.order_repository.get_by_id(order_id)

    def create_order(self, customer: Customer, products: list[Product]):
        order = Order(
            id=self.order_repository.next_id(),
            customer=customer,
            products=products,
        )
        order.calculate_total()
        self.order_repository.save(order)
        return order

    def apply_discount(self, order_id: OrderID, discount_percentage: float):
        order = self.order_repository.get_by_id(order_id)
        order.apply_discount(discount_percentage)
        self.order_repository.save(order)