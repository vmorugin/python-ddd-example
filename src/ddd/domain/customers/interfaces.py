from abc import ABC, abstractmethod

from ddd.domain.customers.models import (
    Order,
    Customer,
)


class CustomerServiceInterface(ABC):
    @abstractmethod
    def get_customer(self, customer_id: int) -> Customer:
        ...

    @abstractmethod
    def create_customer(self, customer_id: int, name: str, email: str) -> Customer:
        ...

    @abstractmethod
    def associate_order(self, customer_id: int, order: Order):
        pass