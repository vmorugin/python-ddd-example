from abc import (
    ABC,
    abstractmethod,
)

from ddd.domain.customers.models import (
    Customer,
    CustomerID,
)


class CustomerServiceInterface(ABC):
    @abstractmethod
    def get_customer(self, customer_id: CustomerID) -> Customer:
        ...

    @abstractmethod
    def create_customer(self, name: str, email: str) -> Customer:
        ...
