class Makanan:
    def __init__(self, nama, daerah):
        self.nama = nama
        self.daerah = daerah

    def khas(self):
        print(self.nama, "makanan khas cirebon")
        
class cirebon(Makanan):
    def __init__(self, nama, karakter, jenis_makanan):
        super().__init__(nama, karakter)
        self.jenis_makanan = jenis_makanan
        
    def rasa(self):
        print("pedas manis")
        
cirebonA = cirebon("tahu gejrot","lontong" , "Berat")
cirebonA.khas() 
cirebonA.rasa() 