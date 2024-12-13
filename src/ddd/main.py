from ddd.infrastructure.adapters.orders.repository import InMemoryOrderRepository
from ddd.infrastructure.adapters.customers.repository import InMemoryCustomerRepository
from ddd.domain.orders.service import OrderService
from ddd.domain.customers.service import CustomerServiceAdapter
from domain.orders.services import DiscountService
from application.orders import OrderApplicationService
from application.customers import CustomerApplicationService

def main():
    order_repository = InMemoryOrderRepository()
    customer_repository = InMemoryCustomerRepository()
    discount_service = DiscountService()

    order_service = OrderService(order_repository, discount_service)
    customer_service = CustomerServiceAdapter(customer_repository)

    order_service_app = OrderApplicationService(order_service, customer_service)
    customer_service_app = CustomerApplicationService(customer_repository)

    customer = customer_service_app.create_customer(1, "John Doe", "john.doe@example.com")

    order_id = 1
    products = [
        {"id": 1, "name": "Product A", "price": 100.0},
        {"id": 2, "name": "Product B", "price": 200.0},
    ]

    order = order_service_app.create_order(order_id, customer.id, products)
    print(f"Order created: {order}")

    updated_order = order_service_app.apply_discount_to_order(order_id, 10)
    print(f"Order after discount: {updated_order}")

if __name__ == "__main__":
    main()
