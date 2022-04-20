from datetime import datetime
from nose.tools import istest, nottest, assert_equal

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'pystregy')))
from pystregy.trader import Trader
from pystregy.model import StrategyRef
from pystregy.config import API_KEY
from tests.scripts.strategy_test import StrategyTest

@istest
def remote_trader():
    name = 'my strategy'
    description = 'strategy description'
    strategy_ref = StrategyRef(
        name=name,
        description=description,
        strategy_type=StrategyTest,
        resources={"model" :"./tests/resources/saved_model.pb"},        
    )

    trader = Trader()
    trader.addstrategy(strategy_ref)

    trader.connect(
        service_url="http://localhost:1234/api", 
        api_key=API_KEY, 
        exg_acc_id='b022e55a-2560-4914-a334-c88a8ab4f50a'
    )

    start_date = datetime(2005, 7, 14)
    end_date = datetime(2005, 7, 15)

    trader.backtest(symbol="BTCUSDT", timeframe=5, start=start_date, end=end_date)