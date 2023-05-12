class makanan:
    def __init__(self, nama,harga):
        self.nama = nama
        self.harga =harga

m = makanan("tape ketan", "50000")

m.khas = "cirebon"

m.harga = "50000"
print(m.nama)
print(m.harga)
print(m.khas)