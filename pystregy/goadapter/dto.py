from datetime import datetime
from decimal import Decimal
from typing import Callable, NamedTuple

class CreatePositionDTO(NamedTuple):
    direction: bool
    open_price: Decimal
    profit_price: Decimal
    loss_price: Decimal
    expiration: datetime

class ClosePositionDTO(NamedTuple):
    id: int
    
class UpdateOrderDTO(NamedTuple):
    id: int
    price: Decimal
    size: Decimal

class CreateOnPriceEventDTO(NamedTuple):
    price: Decimal
    handler: Callable

