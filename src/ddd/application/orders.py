from ddd.domain.orders.interfaces import OrderServiceInterface
from ddd.domain.customers.interfaces import CustomerServiceInterface
from ddd.domain.orders.models import (
    Order,
    Customer as OrderCustomer,
    Product,
)
from ddd.domain.customers.models import Order as CustomerOrder


class OrderApplicationService:
    def __init__(self, order_service: OrderServiceInterface, customer_service: CustomerServiceInterface):
        self.order_service = order_service
        self.customer_service = customer_service

    def get_order(self, order_id: int) -> Order:
        return self.order_service.get_order(order_id)

    def create_order(self, order_id: int, customer_id: int, product_list: list[dict]):
        order = self.order_service.create_order(
            order_id,
            customer=OrderCustomer(id=customer_id),
            products=[
                Product(
                    id=product['id'],
                    price=product['price'],
                    name=product['name'],
                ) for product in product_list
            ]
        )
        self.customer_service.associate_order(
            customer_id,
            order=CustomerOrder(id=order.id)
        )

    def apply_discount_to_order(self, order_id: int, discount_percentage: float):
        return self.order_service.apply_discount(order_id, discount_percentage)
