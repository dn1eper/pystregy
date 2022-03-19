from decimal import Decimal
from datetime import datetime
from .position import Position
from .order import Order

class BrokerBase:
    # actions
    def sell(self, open_price: Decimal, profit_price: Decimal, loss_price: Decimal, expiration: datetime):
        pass

    def buy(self, open_price: Decimal, profit_price: Decimal, loss_price: Decimal, expiration: datetime):
        pass

    def close(self, position: Position):
        pass
    
    def update_order(self, order: Order):
        pass

    # events
    def on_price(self, price: Decimal, handler):
        pass

    # state
    def get_positions(self, pisition_status: int):
        pass

    def get_orders(self, order_status: int):
        pass