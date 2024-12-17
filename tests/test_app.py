from ordering.domain.customers.model import Customer
from ordering.domain.orders.model import Order
from ordering.infrastructure.adapters.orders.repository import InMemoryOrderRepository
from ordering.infrastructure.adapters.customers.repository import InMemoryCustomerRepository
from ordering.application.orders import OrderApplicationService
from ordering.application.customers import CustomerApplicationService
from ordering.infrastructure.adapters.orders.service import (
    OrderCustomerService,
    OrderProductsService,
)


def test_app():
    order_repository = InMemoryOrderRepository()
    customer_repository = InMemoryCustomerRepository()

    customer_service_app = CustomerApplicationService(customer_repository)
    order_service_app = OrderApplicationService(
        order_repository,
        customer_service=OrderCustomerService(customer_service_app),
        products_service=OrderProductsService(),
    )

    customer_id = customer_service_app.create_customer("John Doe", "john.doe@example.com")
    customer = customer_service_app.get_customer(customer_id)
    assert isinstance(customer, Customer)
    assert customer.id == customer_id
    assert customer.name == 'John Doe'
    assert customer.email == 'john.doe@example.com'

    products = [
        {"id": 1, "name": "Product A", "price": 100.0},
        {"id": 2, "name": "Product B", "price": 200.0},
    ]

    order_id = order_service_app.create_order(str(customer.id), products)
    order = order_service_app.get_order(order_id)
    assert isinstance(order, Order)
    assert order.id == order_id
    assert order.calculate_price() == 300
    assert order.customer.id == str(customer_id)

    order_service_app.apply_discount(order_id, 10)
    updated_order = order_service_app.get_order(order_id)
    assert updated_order.calculate_price() == 270
