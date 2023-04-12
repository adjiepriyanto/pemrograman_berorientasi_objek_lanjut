class Bahan:
    def __init__(self, nama, kuantitas):
        self.nama = nama
        self.kuantitas = kuantitas
    
    def __str__(self):
        return f"{self.kuantitas} {self.nama}"
    
class ProdukMinuman:
    def __init__(self, nama, daftar_bahan):
        self.nama = nama
        self.daftar_bahan = daftar_bahan
    
    def tambah_bahan(self, bahan):
        self.daftar_bahan.append(bahan)
        
    def __str__(self):
        return f"{self.nama} terbuat dari: {', '.join(str(bahan) for bahan in self.daftar_bahan)}"
        
        
bahan1 = Bahan("Timun Suri ", "1 kg")
bahan2 = Bahan("susu sachet putih", "38 gram")
bahan3 = Bahan("fanta rasa strawberry", "250 ml")

susu_fanta = ProdukMinuman("Susu fanta", [bahan2, bahan3])
es_timun_suri_strawberry = ProdukMinuman("es timun suri strawberry", [bahan1, bahan3])

print(susu_fanta)
print(es_timun_suri_strawberry)
