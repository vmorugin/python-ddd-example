from ddd.domain.customers.models import (
    Customer,
    CustomerID,
)
from ddd.domain.orders.interfaces import OrderServiceInterface
from ddd.domain.customers.interfaces import CustomerServiceInterface
from ddd.domain.orders.models import (
    Order,
    Customer as OrderCustomer,
    Product,
    OrderID,
)


class OrderApplicationService:
    def __init__(self, order_service: OrderServiceInterface, customer_service: CustomerServiceInterface):
        self.order_service = order_service
        self.customer_service = customer_service

    def get_order(self, order_id: OrderID) -> Order:
        return self.order_service.get_order(order_id)

    def create_order(self, customer_id: CustomerID, product_list: list[dict]) -> OrderID:
        customer = self.customer_service.get_customer(customer_id)
        order = self.order_service.create_order(
            customer=Translator.customer_to_order_customer(customer),
            products=Translator.order_products_from_list_dict(product_list)
        )
        return order.id

    def apply_discount_to_order(self, order_id: OrderID, discount_percentage: float):
        return self.order_service.apply_discount(order_id, discount_percentage)


class Translator:
    @classmethod
    def customer_to_order_customer(cls, customer: Customer) -> OrderCustomer:
        return OrderCustomer(id=str(customer.id))

    @classmethod
    def order_products_from_list_dict(cls, product_list: list[dict]) -> list[Product]:
        return [
                Product(
                    id=product['id'],
                    price=product['price'],
                    name=product['name'],
                ) for product in product_list
            ]
