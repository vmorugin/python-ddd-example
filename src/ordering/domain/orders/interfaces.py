from abc import (
    ABC,
    abstractmethod,
)

from ordering.domain.orders.model import (
    Order,
    Product,
    Customer,
    OrderID,
)


class ICustomerService(ABC):
    @abstractmethod
    def get_customer(self, customer_id: str) -> Customer:
        ...


class IProductsService(ABC):
    @abstractmethod
    def get_products(self, product_list: list[dict]) -> list[Product]:
        ...


class OrderServiceInterface(ABC):
    @abstractmethod
    def get_order(self, order_id: OrderID) -> Order:
        ...

    @abstractmethod
    def create_order(self, customer: Customer, products: list[dict]) -> Order:
        pass

    @abstractmethod
    def apply_discount(self, order_id: OrderID, discount_percentage: float):
        pass
