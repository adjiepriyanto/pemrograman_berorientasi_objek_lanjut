class mobil:
    def __init__(self, nama, cc):
        self.nama = nama
        self.cc = cc
    
    def servis(self):
        print(self.nama, "sedang di servis")

class matic:
    def __init__(self, nama, transmisi):
        self.nama = nama
        self.transmisi = transmisi

    def modif(self):
        print(self.nama, "sedang di modif")

class MobilMatic(mobil, matic):
    def __init__(self, nama, cc, transmisi):
        mobil.__init__(self, nama, cc)
        matic.__init__(self, nama, transmisi)

    def uji(self):
        print(self.nama, "sedang di uji kelayakan")
        
mobil_at =MobilMatic("honda", "150", "Automatic")
mobil_at.servis() 
mobil_at.modif() 
mobil_at.uji() 