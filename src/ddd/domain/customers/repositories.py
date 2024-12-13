from abc import ABC, abstractmethod

from ddd.domain.customers.models import Customer


class CustomerRepository(ABC):
    @abstractmethod
    def save(self, customer):
        pass

    @abstractmethod
    def get_by_id(self, customer_id: int) -> Customer:
        pass