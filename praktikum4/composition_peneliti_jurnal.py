class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
    
    def tulis_jurnal(self, judul, isi):
        jurnal = Jurnal(judul, isi, self)
        return jurnal
    
class Jurnal:
    def __init__(self, judul, isi, penulis):
        self.judul = judul
        self.isi = isi
        self.penulis = penulis

p1 = Peneliti("messi", "sepakbola")


j1 = p1.tulis_jurnal("metode coaching on the run ", "metode ini digunakan pemain sepakbola untuk melihat situasi dalam pertandingan dan berpikir untuk mencari solusi untuk memenangkan pertandingan")


print(j1.judul)
print(j1.penulis.nama)
