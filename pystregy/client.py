import os
import json
import logging
import requests
from datetime import datetime
from pystregy.model import StrategyBase, StrategyRef
from pystregy.strategy_builder import build_strategy

class Client():
    def __init__(self, host: str, port: str, api_key: str, exg_acc_id: str):
        self._host = host
        self._port = port
        self._url = f'http://{host}:{port}/api'
        self._API_KEY = api_key
        self._exg_acc_id = exg_acc_id

    def connect(self): 
        """Check server is up."""
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((self._host, self._port))
        if result != 0:
            raise Exception('Could not connect to server.')

    def _create_strategy(self, sref: StrategyRef) -> str:
        strategy_lib = build_strategy(sref.type, sref.resources, *sref.args, **sref.kwargs)      
        
        headers = {'X-API-Key': self._API_KEY}        
        data = {'name': sref.name, 'description': sref.description}
        files = {
            'json': (None, json.dumps(data), 'application/json'),
            'file': (None, strategy_lib, 'application/octet-stream')
        }        
        r = requests.post(self._url + '/strategy', headers=headers, files=files)

        if r.status_code != 200:
            err_message = ''
            if "error" in r.json():
                err_message = r.json()["error"]
            raise Exception(f'Error creating startegy "{sref.name}": {err_message}')            
        else:
            logging.info(f'Strategy "{sref.name}" id: {r.json()["strategy_id"]}')

        return r.json()["strategy_id"]


    def _strategy_exists(self, id: str) -> bool:
        r = requests.get(self._url + f'/strategy-exists?id={id}')
        if r.json()['response'] == 'true':
            return True
        return False

    def execute_strategy(
        self, strategy_ref: StrategyRef, symbol: str, 
        timeframe: str, start: datetime, end: datetime,
        backtest: bool
    ) -> str | None:
        """Returns strategy execution id if executed successfuly, None otherwise."""
        if strategy_ref.id is None:
            strategy_ref.id = self._create_strategy(strategy_ref)
            if strategy_ref.id is None:
                return

        headers = {'X-API-Key': self._API_KEY, 'Content-Type': 'application/json'}
        json_data = {
            'strategy_id': strategy_ref.id,            
            'timeframe': timeframe,
            'symbol': symbol,
            'start_date': start.strftime('%Y-%m-%d'),
            'end_date': end.strftime('%Y-%m-%d')            
        }

        if backtest:
            url = self._url + '/backtest'
        else:
            url = self._url + '/live-trade'
            json_data |= {'exchange_account_id': self._exg_acc_id}
            raise NotImplementedError()

        resp = requests.post(url, headers=headers, json=json_data)

        if resp.status_code != 200:
            logging.error(f'error executing strategy: {resp.json()["error"]}')
            return
        return resp.json()['strategy_execution_id']
        


