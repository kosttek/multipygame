import asynchat
import logging
import socket
import sys
from threading import Thread


class EchoClient(asynchat.async_chat):
    """Sends messages to the server and receives responses.
    """

    # Artificially reduce buffer sizes to illustrate
    # sending and receiving partial messages.
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64
    
    def __init__(self, host, port):
        self.received_data = []
        self.logger = logging.getLogger('EchoClient')
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.debug('connecting to %s', (host, port))
        self.connect((host, port))
        self.process_data = self._process_my_message
        self.set_terminator('\n')
        return
        
    def handle_connect(self):
        self.logger.debug('handle_connect()')
        thread = Thread(target = self.threaded_send_something())
        thread.start()

    def threaded_send_something(self):
        line = "aaa"
        while line[0] != 'q':
            self.logger.debug('send something')
            # Send the command
            line = sys.stdin.readline()
            self.push('ECHO %s\n' % line)

            # Send the data
            #self.push_with_producer(EchoProducer(self.message, buffer_size=self.ac_out_buffer_size))




    
    def collect_incoming_data(self, data):
        """Read an incoming message from the client and put it into our outgoing queue."""
        self.logger.debug('collect_incoming_data() -> (%d)\n"""%s"""', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        self.logger.debug('found_terminator()')
        received_message = ''.join(self.received_data)
        self.process_data()
        return

    def _process_my_message(self):
        self.logger.debug('bang! end! bang!')
       # self.send_something()

class EchoProducer(asynchat.simple_producer):

    logger = logging.getLogger('EchoProducer')

    def more(self):
        response = asynchat.simple_producer.more(self)
        self.logger.debug('more() -> (%s bytes)\n"""%s"""', len(response), response)
        return response
