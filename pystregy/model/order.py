from enum import IntEnum

class Order:
    CREATED, ACCEPTED, PARTIAL, COMPLETED, CANCELLED, EXPIRED, MARGIN = range(7)

    __slots__ = 'id', 'price', 'size', 'status'

    def __init__(self, id: int, price: float, size: float):
        self.id = id
        self.price = price
        self.size = size
        self.status = self.CREATED
