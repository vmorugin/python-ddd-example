import uuid

from ddd.domain.customers.models import Customer
from ddd.domain.customers.repositories import CustomerRepository

class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self):
        self.customers = {}

    def next_id(self) -> uuid.UUID:
        return uuid.uuid4()

    def save(self, customer):
        self.customers[customer.id] = customer

    def get_by_id(self, customer_id: int) -> Customer:
        return self.customers.get(customer_id)