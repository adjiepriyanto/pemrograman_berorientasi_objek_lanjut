class hewan:
    def move(self):
        print("kuda berlari")

class ikan(hewan):
    def move(self):
        print("ikan berenang")

class kodok(hewan):
    def move(self):
        print("kodok melompat")

H = hewan()
I = ikan()
Ko = kodok()

H.move()    
I.move()    
Ko.move()    