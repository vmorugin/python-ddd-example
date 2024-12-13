from ddd.domain.customers.models import Customer
from ddd.domain.customers.service import CustomerService


class CustomerApplicationService:
    def __init__(self, customer_service: CustomerService):
        self.customer_service = customer_service

    def get_customer(self, customer_id: int) -> Customer:
        customer = self.customer_service.get_customer(customer_id)
        return customer

    def create_customer(self, customer_id: int, name: str, email: str):
        self.customer_service.create_customer(customer_id=customer_id, name=name, email=email)
