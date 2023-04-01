class hewan:
    def __init__(self, nama, species, umur):
        self.nama = nama
        self.species = species
        self.umur = umur

    def gerak(self):
        print(f" {self.species} bernama {self.nama} sedang bergerak.")

    def makan(self):
        print(f" {self.species} bernama {self.nama} sedang makan.")

class mamalia(hewan):
    def __init__(self, nama, species, umur, jml_kaki):
        super().__init__(nama, species, umur)
        self.jml_kaki = jml_kaki

    def melahirkan(self):
        print(f"  {self.species} bernama {self.nama} telah melahirkan.")

class burung(hewan):
    def __init__(self, nama, species, umur, warna_bulu):
        super().__init__(nama, species, umur)
        self.warna_bulu = warna_bulu

    def warna(self):
        print(f" {self.species} bernama {self.nama} memiliki warna bulu {self.warna_bulu} ")

class reptil(hewan):
    def __init__(self, nama, species, umur, habitat):
        super().__init__(nama, species, umur)
        self.habitat = habitat

    def hidup(self):
        print(f" {self.species} bernama {self.nama} banyak hidup di {self.habitat} ")

class harimau(mamalia):
    def __init__(self, nama, umur, ras, jml_kaki):
        super().__init__(nama, "harimau", umur, jml_kaki)
        self.ras = ras

    def mengaum(self):
        print(f" {self.nama} bernama {self.ras} suka mengaum")

class kakatua(burung):
    def __init__(self, nama, umur, warna_bulu, bicara):
        super().__init__(nama, "kakatua", umur, warna_bulu)
        self.bicara = bicara

    def ngomong(self):
        if self.bicara:
            print(f"kakatua bernama {self.nama} suka ngomong")
        else:
            print(f"kakatua bernama {self.nama} ga bisa ngomong")

class buaya(reptil):
    def __init__(self, nama, umur, habitat, berbisa):
        super().__init__(nama, "buaya", umur, habitat)
        self.berbisa = berbisa

    def menggigit(self):
        if self.berbisa:
            print(f"buaya bernama {self.nama} memiliki bisa")
        else:
            print(f"buaya bernama {self.nama} tidak berbisa")

harimau = harimau("billy", 3, "sumatera", 4)
harimau.gerak()
harimau.makan()
harimau.melahirkan()
harimau.mengaum()

kakatua = kakatua("panjul", 3, "jambul putih", True)
kakatua.gerak()
kakatua.makan()
kakatua.warna()
kakatua.ngomong()

buaya = buaya("muara", 3, "rawa-rawa", True)
buaya.gerak()
buaya.makan()
buaya.hidup()
buaya.menggigit()
