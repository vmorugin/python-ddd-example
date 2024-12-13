from abc import ABC, abstractmethod

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass

    @abstractmethod
    def get_by_id(self, order_id: int):
        pass