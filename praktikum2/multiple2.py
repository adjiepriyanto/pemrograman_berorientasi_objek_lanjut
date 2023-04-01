class Motor:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Jenis: {self.jenis}")

class Matic:
    def __init__(self, jenis, transmisi):
        self.jenis = jenis
        self.transmisi = transmisi

    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Transmisi: {self.transmisi}")
class Sport:
    def __init__(self, model, transmisi):
        self.model = model
        self.transmisi = transmisi

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Transmisi: {self.transmisi}")
        

class Ducati (Matic, Sport):
    def __init__(self, nama, jenis, transmisi, model,cc):
        self.cc= cc
        Motor.__init__(self, nama, jenis)
        Matic.__init__(self, jenis, transmisi)
        Sport.__init__(self, model, transmisi)
        
    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"CC: {self.cc}")
       

DucatiA = Ducati("panigale", "Sport", "sport", "v4", "1200")
DucatiA.display_info()