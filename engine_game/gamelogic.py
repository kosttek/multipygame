__author__ = 'kosttek'
class GameLogic:

    transport = 0
    #depricated
    def command(self,(command,data)):
        print("GAMELOGIC: "+command+" "+data) #test

    def receive(self,data):
        print("GAMELOGIC: "+data)             #test
    self.write("GAMELOGIC --> done!")         #test

    def write(self,data):
        self.transport.write(data)

    def setTransport(self,tra):
        self.transport = tra;
