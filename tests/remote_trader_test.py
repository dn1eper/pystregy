import logging
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
    logging.basicConfig(level=logging.INFO)

    name = 'my strategy'
    description = 'strategy description'
    strategy_ref = StrategyRef(
        strategy_type=StrategyTest,
        resources={"model" :"./tests/resources/saved_model.pb"},        
    )

    trader = Trader()
    trader.addstrategy(strategy_ref)

    trader.connect(
        host='localhost',
        port=1234,
        api_key=API_KEY, 
    )

    start_date = datetime(2005, 7, 14)
    end_date = datetime(2005, 7, 15)

    trader.backtest(symbol="BTCUSDT", timeframe_sec=5*60, start=start_date, end=end_date)