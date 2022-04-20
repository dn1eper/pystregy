from datetime import datetime
from nose.tools import istest, nottest, assert_equal
from pystregy.client import Client
from pystregy.model import StrategyRef

from tests.scripts.strategy_test import StrategyTest

@istest
def client_test():
    strategy_ref = StrategyRef(StrategyTest, {"model" :"./tests/resources/saved_model.pb"}, False, param=True)
    strategy_ref.set_name("test name")
    strategy_ref.set_description("test description")

    client = Client("http://localhost:8080/api", "TOKEN")
    
    print(client._create_strategy(strategy_ref))
