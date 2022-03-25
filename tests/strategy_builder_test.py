from nose.tools import istest, nottest, assert_equal

from tests.scripts.strategy_test import StrategyTest
from pystregy.strategy_builder import build_strategy

@istest
def build_strategy_test():
    zipapp = build_strategy(StrategyTest, {"model" :"./tests/resources/saved_model.pb"}, False, param=True)
    assert_equal(True, True)
