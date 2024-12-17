from uuid import UUID

from ordering.domain.customers.interfaces import CustomerServiceInterface
from ordering.domain.customers.model import (
    Customer,
    CustomerID,
)
from ordering.domain.orders.interfaces import (
    ICustomerService,
    IProductsService,
)
from ordering.domain.orders.model import (
    Customer as OrderCustomer,
    Product,
)


class OrderCustomerService(ICustomerService):
    def __init__(self, customer_service: CustomerServiceInterface):
        self._service = customer_service

    def get_customer(self, customer_id: str) -> Customer:
        return Translator.customer_to_order_customer(self._service.get_customer(CustomerID(UUID(customer_id))))


class OrderProductsService(IProductsService):
    def get_products(self, product_list: list[dict]) -> list[Product]:
        return Translator.order_products_from_list_dict(product_list)


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
