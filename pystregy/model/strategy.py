from pystregy.model import Order, Position, BrokerBase

class StrategyRef():
    def __init__(self, id: str):
        self._id = id

    def __init__(self, name: str, description: str):
        self._id = None
        self._name = name
        self._description = description

    def has_id(self):
        return self._id != None


class StrategyBase(StrategyRef):
    def __init__(self, broker: BrokerBase):
        self.broker = broker

    def notify_position(self, position: Position):
        pass

    def notify_order(self, order: Order):
        pass
   