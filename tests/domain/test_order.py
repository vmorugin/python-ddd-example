import uuid

import pytest

from ordering.domain.orders.model import (
    Order,
    OrderID,
    Customer,
    Product,
)


class TestOrderModel:
    @pytest.fixture
    def get_product(self):
        def wrapper(
                product_id: str = None,
                name: str = None,
                price: float = 0.0,
        ):
            return Product(
                id=product_id or str(uuid.uuid4()),
                name=name or str(uuid.uuid4()),
                price=price
            )

        return wrapper

    @pytest.fixture
    def get_order(self):
        def wrapper(
                order_id: OrderID = None,
                customer: Customer = None,
                products: list[Product] = None,
                discount: float = 0.0,
        ):
            return Order(
                id=order_id or OrderID.generate(),
                customer=customer or Customer(id=str(uuid.uuid4())),
                products=products or [],
                discount=discount,
            )

        return wrapper

    def test_order_id(self):
        order_id = OrderID.generate()
        assert isinstance(order_id, OrderID)

    def test_order_id_eq(self):
        key = uuid.uuid4()
        assert OrderID(key) == OrderID(key)

    def test_order_id_neq(self):
        assert OrderID.generate() != OrderID.generate()

    def test_init(self):
        customer = Customer(id='test-id')
        model = Order(id=OrderID.generate(), customer=customer)
        assert model.calculate_price() == 0
        assert model.discount == 0
        assert model.products == []
        assert model.customer == customer

    def test_count_price(self, get_order, get_product):
        order = get_order(products=[get_product(price=10), get_product(price=2.2)])
        assert order.calculate_price() == 12.2

    def test_count_price_with_discount(self, get_order, get_product):
        order = get_order(products=[get_product(price=100), get_product(price=200)], discount=5)
        assert order.calculate_price() == 285.0
