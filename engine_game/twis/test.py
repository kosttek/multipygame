__author__ = 'kosttek'
from time import sleep
from threading import Thread
class myClass():

    # def help(self):
    #
    #     os.system('./ssh.py')

    def nope(self):
        a = [1,2,3,4,5,6,67,78]
        for i in a:
            print i
            sleep(1)

    def thr(self):
        thread = Thread(target = self.nope)
        thread2 = Thread(target = self.nope)
        thread3 = Thread(target = self.nope)
        thread4 = Thread(target = self.nope)
        thread.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread.join()
if __name__ == "__main__":
    Yep = myClass()
    Yep.thr()
    print 'Finished'