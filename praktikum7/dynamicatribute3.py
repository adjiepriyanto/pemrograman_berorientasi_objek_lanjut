class tumbuhan:
    def __init__(self, nama,jenis):
        self.nama = nama
        self.jenis =jenis

t = tumbuhan("eceng gondok", "hidrofit")

t.habitat = "air"

t.jenis = "hidrofit"
print(t.nama)
print(t.jenis)
print(t.habitat)