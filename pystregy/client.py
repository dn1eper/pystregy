from datetime import datetime
from pystregy.model import StrategyBase, StrategyRef
from pystregy.strategy_builder import build_strategy

class Client():
    def __init__(self, url: str, token: str):
        self._url = url
        # TODO: connects

    def _create_strategy(self, strategy_ref: StrategyRef):
        strategy_lib = build_strategy(strategy_ref.type, strategy_ref.resources, *strategy_ref.args, **strategy_ref.kwargs)
        #strategy_ref.id = 
        raise NotImplementedError() #TODO:create strategy request

    def execute_strategy(self, strategy_ref: StrategyRef):
        if strategy_ref.id is None:
            self._create_strategy(strategy_ref)


        raise NotImplementedError() #TODO: execute request


