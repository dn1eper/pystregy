import os
import sys
import base64
from typing import Dict
import stickytape
import zipapp
from pystregy.utils import clear_dir

TMP_ZIPAPP_PATH: str = "./build/zipapp"

def build_strategy(strategy_type: type, resource_paths: Dict[str, str], *args, **kwargs) -> bytes:
    bundle = _create_bundle(strategy_type, resource_paths, *args, **kwargs)
    return _make_zipapp(bundle)

def _create_bundle(strategy_type: type, resource_paths: Dict[str, str], *args, **kwargs) -> str:
    # create strategy source code bundle
    strategy_path = os.path.abspath(sys.modules[strategy_type.__module__].__file__)
    source_bundle = stickytape.script(strategy_path)

    # load resources
    resources = dict()
    for res_key, res_path in resource_paths.items():
        with open(res_path, 'rb') as file:
            file_body = file.read()
            resources[res_key] = base64.b64encode(file_body)

    # args and kwargs
    args_str = ", ".join([repr(a) for a in args])
    if args_str:
        args_str = "," + args_str
    kwargs_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    if kwargs_str:
        kwargs_str = "," + kwargs_str

    # generate strategy initialisation code
    init_strategy_code = f"""
import base64
from pystregy.goadapter import GoBroker
from pystregy.model import Order, Position
from pystregy.utils import tojson

__resources = dict((_k, base64.b64decode(_v)) for _k, _v in {resources}.items())
__broker = GoBroker()
__strategy = {strategy_type.__name__}(__broker, __resources {args_str} {kwargs_str})

def notify_position(position: Position) -> str:
    __strategy.notify_position(position)
    return tojson(__broker.get_commands_queue())

def notify_order(order: Order) -> str: 
    __strategy.notify_order(order)
    return tojson(__broker.get_commands_queue())
"""
    return source_bundle + init_strategy_code

def _make_zipapp(bundle: str) -> bytes:
    # create or clear target dir
    if not os.path.exists(TMP_ZIPAPP_PATH):
        os.makedirs(TMP_ZIPAPP_PATH)
    else:
        clear_dir(TMP_ZIPAPP_PATH)
    
    # create temp file with source code
    bundle_path = f'{TMP_ZIPAPP_PATH}/__main__.py'
    with open(bundle_path, 'w+') as file:
        file.write(bundle)

    # create zipapp archive
    zipapp_path = f'{TMP_ZIPAPP_PATH}/strategy.pyz'
    zipapp.create_archive(TMP_ZIPAPP_PATH, zipapp_path)

    file = open(zipapp_path, "rb")
    bytes_read = file.read()
    file.close()

    clear_dir(TMP_ZIPAPP_PATH)

    return bytes_read
