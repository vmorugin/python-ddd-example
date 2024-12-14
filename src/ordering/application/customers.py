from ordering.domain.customers.model import (
    Customer,
    CustomerID,
)
from ordering.domain.customers.service import CustomerService


class CustomerApplicationService:
    def __init__(self, customer_service: CustomerService):
        self.customer_service = customer_service

    def get_customer(self, customer_id: CustomerID) -> Customer:
        customer = self.customer_service.get_customer(customer_id)
        return customer

    def create_customer(self, name: str, email: str):
        customer = self.customer_service.create_customer(name=name, email=email)
        return customer.id
