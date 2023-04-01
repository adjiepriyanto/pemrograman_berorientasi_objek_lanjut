class Motor:
    def __init__(self, nama, cc):
        self.nama = nama
        self.cc = cc

    def kecepatan(self):
        print(f"{self.nama} berkecepatan tinggi")

class yamaha(Motor):
    def __init__(self, nama, cc, jenis):
        super().__init__(nama, cc)
        self.jenis = jenis

    def balapan(self):
        print(f"{self.nama} dengan jenis {self.jenis} sedang balapan")
        
yamahaA = yamaha("r7", 250, "R")
yamahaA.kecepatan() 
yamahaA.balapan() 