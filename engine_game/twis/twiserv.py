__author__ = 'kosttek'


# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol
from engine_game import gamelogic
from threading import Thread
from time import sleep

class ServerProtocol(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    """transport is set to gameserver(gamelogic) because game logic use it to write back"""
    def connectionMade(self):
        self.factory.gameserver.setTransport(self.transport)

    def dataReceived(self, data):
        if self.factory.gameserver != 0 :
            self.factory.gameserver.receive(data)



class ServerFactory(protocol.Factory):
    protocol = ServerProtocol
    gameserver = 0

    def __init__(self,gameserver):
        self.gameserver = gameserver

def main():
    """This runs the protocol on port 8000"""
    factory = ServerFactory(gamelogic.GameLogic())
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()