from datetime import datetime
from pystregy.model.strategy import StrategyBase, StrategyRef
from pystregy.client import Client
import itertools

class Trader():
    def __init__(self, is_remote: bool=True):
        self._strats = list()
        self._service = None
        self._service_url = None
        self._is_remote = is_remote

    def connect(self, service_url: str, token: str):
        self._service_url = service_url
        self._service = Client(service_url, token)

    def addstrategy(self, strategy: type, *args, **kwargs):
        self._strats.append((strategy, args, kwargs))
        return len(self._strats) - 1

    def addstrategy_ref(self, strategy_ref: StrategyRef, *args, **kwargs):
        self._strats.append((strategy_ref, args, kwargs))
        return len(self._starts) - 1

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

        iterstrats = itertools.product(*self._strats)
        for stratcls, sargs, skwargs in iterstrats:
            strat_ref = None
            if isinstance(stratcls, StrategyBase):
                strat_ref = self._service.create_strategy(stratcls)
            elif isinstance(stratcls, StrategyRef):
                strat_ref = stratcls
            else:
                raise ValueError("not compatible strategy type")

            backtest_execution_id = self._service.run_backtester(strat_ref)
            
            

            
