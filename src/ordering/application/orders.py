from ordering.domain.orders.interfaces import (
    OrderServiceInterface,
    ICustomerService,
    IProductsService,
)
from ordering.domain.orders.model import (
    OrderID,
    Order,
)
from ordering.domain.orders.repository import OrderRepository


class OrderApplicationService(OrderServiceInterface):
    def __init__(
            self,
            order_repository: OrderRepository,
            customer_service: ICustomerService,
            products_service: IProductsService,
    ):
        self.order_repository = order_repository
        self.customer_service = customer_service
        self.product_service = products_service

    def get_order(self, order_id: OrderID) -> Order:
        return self.order_repository.get_by_id(order_id)

    def create_order(self, customer_id: str, product_list: list[dict]) -> OrderID:
        customer = self.customer_service.get_customer(customer_id)
        product = self.product_service.get_products(product_list)
        order = Order(
            id=self.order_repository.next_id(),
            customer=customer,
            products=product,
        )
        self.order_repository.save(order)
        return order.id

    def apply_discount(self, order_id: OrderID, discount_percentage: float):
        order = self.order_repository.get_by_id(order_id)
        order.apply_discount(discount_percentage)
        self.order_repository.save(order)
