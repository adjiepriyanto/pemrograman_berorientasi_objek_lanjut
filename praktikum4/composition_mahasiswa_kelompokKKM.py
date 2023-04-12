class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None
    
    def gabung_kelompok(self, kelompok):
        self.kelompok = kelompok
        kelompok.tambah_anggota(self)
    
class KelompokKKM:
    def __init__(self, nama):
        self.nama = nama
        self.anggota = []
    
    def tambah_anggota(self, anggota):
        self.anggota.append(anggota)

m1 = Mahasiswa("messi", "121212")
k2 = KelompokKKM("Kelompok 2")
m1.gabung_kelompok(k2)


print(k2.nama)
for anggota in k2.anggota:
    print(anggota.nama)
