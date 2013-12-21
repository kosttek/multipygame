__author__ = 'kosttek'


# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol
from threading import Thread
from time import sleep

class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    thread_bool = False

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("received: "+data)
        self.transport.write(data)
        if not self.thread_bool:
            thread = Thread(target = self.write_junk)
            thread.start()
            self.thread_bool = True

    def write_junk(self):
        while True:
            sleep(2)
            self.transport.write("junk")


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()