class Hewan:
    def __init__(self, nama, species, suara):
        self.nama = nama
        self.species = species
        self.suara = suara

    def bersuara(self):
        print(self.suara)


class reptil(Hewan):
    def __init__(self, nama, species, suara, kaki):
        super().__init__(nama, species, suara)
        self.kaki = kaki

    def berjalan(self):
        print(f"{self.nama} berjalan dengan {self.kaki} kaki.")


class iguana(reptil):
    def __init__(self, nama, ras, kaki):
        super().__init__(nama, "iguana", "iguana gurun", kaki)
        self.ras = ras

    def melengking(self):
        print(f"{self.nama} bersuara melengking.")


class kadal(reptil):
    def __init__(self, nama, ras, kaki):
        super().__init__(nama, "kadal", "kadal air", kaki)
        self.ras = ras

    def mengejar(self):
        print(f"{self.nama} mengejar.")


iguanaA = iguana("iguana", "air", 4)
kadalA = kadal("kadal", "air", 2)

iguanaA.bersuara()
iguanaA.berjalan()
iguanaA.melengking()

print("------------------------")

kadalA.bersuara()
kadalA.berjalan()
kadalA.mengejar()
