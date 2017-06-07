import json
import os
from pprint import pprint

__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

conf_json = None
try:
    with open(os.path.join(__location__,'../config.json')) as conf:
        conf_json = json.load(conf)
except FileNotFoundError: 
    with open(os.path.join(__location__,'./config/default_config.json')) as conf:
        conf_json = json.load(conf)

pprint(conf_json)

def test_config_read():
    print("\nTEST: test_config_read")
    pprint(conf_json["classBaseStats"]["rogue"])
