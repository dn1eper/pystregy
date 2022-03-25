from datetime import datetime
from decimal import Decimal
from typing import Callable
from pystregy.goadapter.repository import Repository
from pystregy.model.broker import BrokerBase
from pystregy.goadapter.dto import CreatePositionDTO, ClosePositionDTO, CreateOnPriceEventDTO, UpdateOrderDTO
from pystregy.model.order import Order
from pystregy.model.position import Position
from pystregy.utils import todict
import json

class Broker(BrokerBase):
    def __init__(self):
        self.repo = Repository()

    def sell(self, open_price: Decimal, profit_price: Decimal, loss_price: Decimal, expiration: datetime):
        self.repo.position.create.append(
            CreatePositionDTO(
                direction=0,
                open_price=open_price,
                profit_price=profit_price,
                loss_price=loss_price,
                expiration=expiration
            )
        )

    def buy(self, open_price: Decimal, profit_price: Decimal, loss_price: Decimal, expiration: datetime):
        self.repo.position.create.append(
            CreatePositionDTO(
                direction=1,
                order_price=open_price,
                profit_price=profit_price,
                loss_price=loss_price,
                expiration=expiration
            )
        )

    def close(self, position: Position):
        self.repo.position.close.append(
            ClosePositionDTO(position.id)
        )
    
    def update_order(self, order: Order):
        self.repo.orders.append(
            UpdateOrderDTO(
                id=order.id,
                price=order.price,
                size=order.size
            )
        )

    def on_price(self, price: Decimal, handler: Callable):
        self.repo.events.on_price.append(
            CreateOnPriceEventDTO(
                price=price,
                handler=handler
            )
        )

    def get_commands_queue(self, clear: bool=True) -> str:
        repo_dict = todict(self.repo)
        if clear:
            self.repo = Repository()
        return repo_dict
