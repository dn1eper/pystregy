import logging
import requests
from datetime import datetime
from pystregy.model.strategy import StrategyBase, StrategyRef
from pystregy.client import Client

class Trader():
    def __init__(self, is_remote: bool=True):
        self._strats = []
        self._service = None
        self._is_remote = is_remote

    def connect(self, host: str, port: str, api_key: str, exg_acc_id=None) -> bool:
        self._service = Client(host, port, api_key, exg_acc_id)
        return self._service.connect()        

    def addstrategy(self, strategy_ref: StrategyRef, *args, **kwargs):
        self._strats.append(strategy_ref)
        return len(self._strats) - 1

    def run(self):
        pass

    def backtest(self, symbol: str, timeframe: int, start: datetime, end: datetime):
        if (24 * 60 * 60) % timeframe != 0:
            logging.error('incorrect timeframe (86400 % timeframe should be zero)')            
            
        if self._is_remote:
            self._backtest_remote(symbol, timeframe, start, end)
        else:
            self._backtest_local(symbol, timeframe, start, end)

    def _backtest_local(self, symbol: str, timeframe: str, start: datetime, end: datetime):
        raise NotImplementedError()

    def _backtest_remote(self, symbol: str, timeframe: str, start: datetime, end: datetime):
        for strat in self._strats:
            self._service.execute_strategy(strat, symbol, timeframe, start, end, backtest=True)
            
            
