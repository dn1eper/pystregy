from datetime import datetime
from pystregy.model.strategy import StrategyBase, StrategyRef
from pystregy.client import Client

class Trader():
    def __init__(self, is_remote: bool=True):
        self._strats = list()
        self._service = None
        self._service_url = None
        self._is_remote = is_remote

    def connect(self, service_url: str, token: str):
        self._service_url = service_url
        self._service = Client(service_url, token)

    def addstrategy(self, strategy_ref: StrategyRef, *args, **kwargs):
        self._strats.append(strategy_ref)
        return len(self._strats) - 1

    def run(self):
        pass

    def backtest(self, symbol: str, start: datetime, end: datetime):
        if self._is_remote:
            self._backtest_remote(symbol, start, end)
        else:
            self._backtest_local(symbol, start, end)

    def _backtest_local(self, symbol: str, start: datetime, end: datetime):
        raise NotImplementedError()

    def _backtest_remote(self, symbol: str, start: datetime, end: datetime):

        for strat in self._strats:
            execution_id = self._service.execute_strategy(strat)
            
            
