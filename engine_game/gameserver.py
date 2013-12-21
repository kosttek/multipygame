__author__ = 'kosttek'
import asyncore
import logging
import sys

from asyn.asyn_server import EchoServer
from gamelogic import GameLogic
#from asyn.asyn_client import EchoClient
import twis.twiserv
from twisted.internet import reactor, protocol
import gamelogic
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(name)s: %(message)s',
#                     )
#
# address = ('localhost', 19991) # let the kernel give us a port
# server = EchoServer(address,GameLogic())
# ip, port = server.address # find out what port we were given
# #
# # message_data = open('asyn/lorem.txt', 'r').read()
# # client = EchoClient(ip, port, message=message_data)
#
# asyncore.loop()


gamelogic = GameLogic()
factory = protocol.ServerFactory()
echo = twis.twiserv.Echo()
factory.protocol = echo
echo.set_gameserver(gamelogic)
reactor.listenTCP(8000,factory)
reactor.run()