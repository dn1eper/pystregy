from enum import IntEnum

from .order import Order

class Status(IntEnum):
     OPEN = 0
     TAKE_PROFIT = 1
     STOP_LOSS = 2
     CANCELLED = 3

class Position():
    __slots__ = 'id', 'main_order', 'take_order', 'stop_order', 'status'

    def __init__(self, 
        id: int, 
        main_order: Order, 
        take_order: Order,
        stop_order: Order,
    ):
        self.id = id
        self.main_order = main_order
        self.take_order = take_order
        self.stop_order = stop_order
        self.status = Status.OPEN
