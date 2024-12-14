import typing as t
from dataclasses import (
    dataclass,
)
from uuid import UUID

CustomerID = t.NewType('CustomerID', UUID)


@dataclass(kw_only=True, frozen=True)
class Customer:
    id: CustomerID
    name: str
    email: str
