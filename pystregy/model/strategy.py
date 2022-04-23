from typing import Dict

from pystregy.model import Order, Position, BrokerBase, Quote

class StrategyRef():
    def __init__(self, id: str):
        self.id = id

    def __init__(self, strategy_type: type, resources: Dict[str, str], *args, **kwargs):
        self.id = None
        self.type = strategy_type
        self.resources = resources
        self.args = args
        self.kwargs = kwargs

    def set_name(self, name: str):
        self.name = name

    def set_description(self, description: str):
        self.description = description
    

class StrategyBase():
    def __init__(self, broker: BrokerBase, resources: Dict[str, str]):
        self.broker = broker
        self.resources = resources

    def on_position(self, position: Position):
        pass

    def on_order(self, order: Order):
        pass

    def on_quote(self, quote: Quote):
        pass
   