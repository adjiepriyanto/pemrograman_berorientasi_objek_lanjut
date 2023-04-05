from abc import ABC, abstractmethod

class makanan(ABC):
    @abstractmethod
    def start(self):
        pass

class tahu(makanan):
    def start(self):
        print("tahu dimasak dengan di goreng")

class mie(makanan):
    def start(self):
        print("mie dimasak dengan direbus")

class bolu(makanan):
    def start(self):
        print("bolu dimasak dengan dikukus")



T = tahu()
Mi = mie()
B = bolu()

T.start()    
Mi.start()    
B.start()    
