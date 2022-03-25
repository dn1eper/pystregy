from typing import Dict

from pystregy.model import Order, Position, BrokerBase

class StrategyRef():
    def __init__(self, id: str, name: str=None, description: str=None):
        self.id = id
        self.name = name
        self.description = description

    def __init__(self, strategy_type: type, resources: Dict[str, str], *args, **kwargs):
        self.id = None
        self.type = strategy_type
        self.resources = resources
        self.args = args
        self.kwargs = kwargs


class StrategyBase():
    def __init__(self, broker: BrokerBase, resources: Dict[str, str]):
        self.broker = broker
        self.resources = resources

    def notify_position(self, position: Position):
        pass

    def notify_order(self, order: Order):
        pass
   