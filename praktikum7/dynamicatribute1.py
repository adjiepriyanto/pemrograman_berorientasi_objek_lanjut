class motor:
    def __init__(self, jenis,merk):
        self.jenis = jenis
        self.merk =merk

m = motor("KTM 450 EXC-F Six Days", "KTM")

m.cc = "450 cc"

m.merk = "KTM"
print(m.jenis)
print(m.merk)
print(m.cc)