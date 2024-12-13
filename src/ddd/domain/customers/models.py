from dataclasses import (
    dataclass,
    field,
)

@dataclass(kw_only=True, frozen=True)
class Order:
    id: int


@dataclass(kw_only=True, frozen=True)
class Customer:
    id: int
    name: str
    email: str
    orders: list[Order] = field(default_factory=list)

    def add_order(self, order: Order):
        self.orders.append(order)