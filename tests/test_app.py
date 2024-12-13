from ddd.domain.customers.models import Customer
from ddd.domain.orders.models import Order
from ddd.infrastructure.adapters.orders.repository import InMemoryOrderRepository
from ddd.infrastructure.adapters.customers.repository import InMemoryCustomerRepository
from ddd.domain.orders.service import OrderService
from ddd.domain.customers.service import CustomerService
from ddd.application.orders import OrderApplicationService
from ddd.application.customers import CustomerApplicationService


def test_app():
    order_repository = InMemoryOrderRepository()
    customer_repository = InMemoryCustomerRepository()

    order_service = OrderService(order_repository)
    customer_service = CustomerService(customer_repository)

    order_service_app = OrderApplicationService(order_service, customer_service)
    customer_service_app = CustomerApplicationService(customer_service)

    customer_service_app.create_customer(1, "John Doe", "john.doe@example.com")
    customer = customer_service_app.get_customer(1)
    assert isinstance(customer, Customer)
    assert customer.id == 1
    assert customer.name == 'John Doe'
    assert customer.email == 'john.doe@example.com'
    assert customer.orders == []

    order_id = 1
    products = [
        {"id": 1, "name": "Product A", "price": 100.0},
        {"id": 2, "name": "Product B", "price": 200.0},
    ]

    order_service_app.create_order(order_id, customer.id, products)
    order = order_service_app.get_order(order_id)
    assert isinstance(order, Order)
    assert order.id == 1
    assert order.total == 300
    assert order.customer.id == 1

    order_service_app.apply_discount_to_order(order_id, 10)
    updated_order = order_service_app.get_order(order_id)
    assert updated_order.total == 270

    customer = customer_service_app.get_customer(1)
    assert len(customer.orders) == 1
    assert customer.orders[0].id == 1