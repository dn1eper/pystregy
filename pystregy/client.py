from datetime import datetime
from pystregy.model import StrategyBase, StrategyRef

class Client():
    def __init__(self, url: str, token: str):
        self._url = url
        # TODO: connects

    def create_strategy(self, strategy: StrategyBase) -> StrategyRef:
        raise NotImplementedError()

    def init_strategy(self):
        raise NotImplementedError()

    def run_backtester(self, strategy_ref: StrategyRef) -> str:
        raise NotImplementedError()


