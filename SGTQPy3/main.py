#!/usr/bin/python3

import json
import os
from pprint import pprint
from bot import bot

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    conf_json = None
    try:
        with open(os.path.join(__location__,'./config.json')) as conf:
            conf_json = json.load(conf)
    except FileNotFoundError: 
        with open(os.path.join(__location__,'./config/default_config.json')) as conf:
            conf_json = json.load(conf)

    pprint(conf_json)
    #start the bot up
    # this secret will eventually be read from the config file, maybe
    bot.runbot('MzA1OTM2NjMwMzgyOTg1MjE3.C98edg.9bPTOe4-aB5Xk0PLeWtAhxCILFo')

if __name__ == '__main__':
    main()