from ddd.domain.customers.interfaces import CustomerServiceInterface
from ddd.domain.customers.models import (
    Order,
    Customer,
)
from ddd.domain.customers.repositories import CustomerRepository



class CustomerService(CustomerServiceInterface):
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def get_customer(self, customer_id: int) -> Customer:
        return self.customer_repository.get_by_id(customer_id)

    def associate_order(self, customer_id: int, order: Order):
        customer = self.customer_repository.get_by_id(customer_id)
        customer.add_order(order)
        self.customer_repository.save(customer)

    def create_customer(self, customer_id: int, name: str, email: str) -> Customer:
        customer = Customer(id=customer_id, name=name, email=email)
        self.customer_repository.save(customer)
        return customer
