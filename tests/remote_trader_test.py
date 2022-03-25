from datetime import datetime
from nose.tools import istest, nottest, assert_equal
from pystregy.trader import Trader
from pystregy.model import StrategyRef

from tests.scripts.strategy_test import StrategyTest

@istest
def remote_trader():

    strategy_ref = StrategyRef(StrategyTest, {"model" :"./tests/resources/saved_model.pb"}, False, param=True)

    trader = Trader()
    trader.addstrategy(strategy_ref)

    trader.connect("http://localhost:8080/api", "TOKEN")

    start_date = datetime(2005, 7, 14, 12, 30)
    end_date = datetime(2005, 7, 14, 12, 30)

    trader.backtest("BTCUSDT", start_date, end_date)

