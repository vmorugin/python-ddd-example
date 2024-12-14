from ddd.domain.customers.interfaces import CustomerServiceInterface
from ddd.domain.customers.models import (
    Customer,
    CustomerID,
)
from ddd.domain.customers.repositories import CustomerRepository



class CustomerService(CustomerServiceInterface):
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def get_customer(self, customer_id: CustomerID) -> Customer:
        return self.customer_repository.get_by_id(customer_id)

    def create_customer(self, name: str, email: str) -> Customer:
        customer = Customer(
            id=self.customer_repository.next_id(),
            name=name,
            email=email
        )
        self.customer_repository.save(customer)
        return customer
