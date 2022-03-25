from pystregy.model import StrategyBase, Position, Order
from datetime import datetime

class StrategyTest(StrategyBase):
    def __init__(self, broker, resouces, flag, param=None):
        super(StrategyTest, self).__init__(broker, resouces)
        self.flag = flag
        self.param = param

    def notify_position(self, position: Position):
        print("notify_position " + str(self.flag))
        print(self.resouces["model"])
        self.broker.sell(1, 2, 3, datetime.now())
        pass

    def notify_order(self, order: Order):
        print("notify_order " + str(self.flag))
        self.flag = False
        
