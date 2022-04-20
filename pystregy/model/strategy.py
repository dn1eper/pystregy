from typing import Dict

from pystregy.model import Order, Position, BrokerBase, Quote

class StrategyRef():
    def __init__(self, id: str):
        self.id = id

    def __init__(self,
        name: str, description: str, 
        strategy_type: type, resources: Dict[str, str], *args, **kwargs
    ):
        self.id = None
        self.name = name
        self.description = description
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

    def notify_quote(self, quote: Quote):
        pass
   