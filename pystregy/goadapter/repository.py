from pystregy.goadapter.dto import CreatePositionDTO, ClosePositionDTO, UpdateOrderDTO, CreateOnPriceEventDTO
from typing import List, NamedTuple

class PositionRepository(dict):
    def __init__(self):
        self.create = list()
        self.create = list()

    create: List[CreatePositionDTO]
    close: List[ClosePositionDTO]

class OrderRepository(dict):
    def __init__(self):
        self.update = list()

    update: List[UpdateOrderDTO]

class EventRepository(dict):
    def __init__(self):
        self.on_price = list()

    on_price: List[CreateOnPriceEventDTO]

class Repository(dict):
    def __init__(self):
        self.position = PositionRepository()
        self.order = OrderRepository()
        self.event = EventRepository()

    position: PositionRepository
    order: OrderRepository
    event: EventRepository
