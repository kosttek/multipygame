__author__ = 'kosttek'
import asyncore
import logging
import sys

from asyn.asyn_server import EchoServer
from gamelogic import GameLogic
from asyn.asyn_client import EchoClient



logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )



client = EchoClient("localhost", 19991)

asyncore.loop()
