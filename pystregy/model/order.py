from enum import IntEnum

class Status(IntEnum):
    CREATED = 0
    ACCEPTED = 1
    PARTIAL = 2
    COMPLETED = 3
    CANCELLED = 4
    EXPIRED = 5
    MARGIN = 6

class Order():
    __slots__ = 'id', 'price', 'size', 'status'

    def __init__(self, id: int, price: float, size: float):
        self.id = id
        self.price = price
        self.size = size
        self.status = Status.CREATED