class pegawai:
    def __init__(self, nama, umur, gaji):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji

    def display_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("Gaji:", self.gaji)


class Manager(pegawai):
    def __init__(self, name, umur, gaji, divisi):
        super().__init__(name, umur, gaji)
        self.divisi = divisi

    def display_info(self):
        super().display_info()
        print("Divisi:", self.divisi)


class SalesManager(Manager):
    def __init__(self, nama, umur, gaji, divisi, bonus):
        super().__init__(nama, umur, gaji, divisi)
        self.bonus = bonus

    def display_info(self):
        super().display_info()
        print("Bonus:", self.bonus)


class HRManager(Manager):
    def __init__(self, nama, umur, gaji, divisi, tunjangan):
        super().__init__(nama, umur, gaji, divisi)
        self.tunjangan = tunjangan

    def display_info(self):
        super().display_info()
        print("Tunjangan:", self.tunjangan)


pegawaiA = pegawai("susi susanti", 20, 5000)
managerA = Manager("taufik hidayat", 30, 10000, "Marketing")
smA = SalesManager("antony ginting", 35, 15000, "Marketing", 5000)
hrA = HRManager("jonathan cristie", 40, 20000, "HR", 10000)

pegawaiA.display_info()
print("------------------------")
managerA.display_info()
print("------------------------")
smA.display_info()
print("------------------------")
hrA.display_info()
