from abc import ABC, abstractmethod

from ddd.domain.customers.models import (
    Customer,
    CustomerID,
)


class CustomerRepository(ABC):
    @abstractmethod
    def next_id(self) -> CustomerID:
        ...

    @abstractmethod
    def get_by_id(self, customer_id: CustomerID) -> Customer:
        pass

    @abstractmethod
    def save(self, customer: Customer):
        pass