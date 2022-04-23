from datetime import datetime
from .position import Position
from .order import Order

class BrokerBase:
    # actions
    def sell(self, open_price: float, profit_price: float, loss_price: float, expiration: datetime):
        pass

    def buy(self, open_price: float, profit_price: float, loss_price: float, expiration: datetime):
        pass

    def close(self, position: Position):
        pass
    
    def update_order(self, order: Order):
        pass

    # events
    def on_price(self, price: float, handler):
        pass

    # state
    def get_positions(self, pisition_status: int):
        pass

    def get_orders(self, order_status: int):
        pass