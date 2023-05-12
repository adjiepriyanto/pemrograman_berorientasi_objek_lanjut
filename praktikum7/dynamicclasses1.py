def custom_aksesoris(tipe_aksesoris):
    class aksesoris:
        def __init__(self, brand, warna):
            self.tipe_aksesoris = tipe_aksesoris
            self.brand = brand
            self.warna = warna

        def __repr__(self):
            return f"{self.brand} {self.tipe_aksesoris} ({self.warna})"

    return aksesoris


Hat = custom_aksesoris("Topi")
Mug = custom_aksesoris("gelas")


Hat1 = Hat("Trucker hat", "hitam")
Hat2 = Hat("Beanie", "silver")

Mug1 = Mug("sango", "biru")
Mug2 = Mug("zen", "putih")

print(Hat1)  
print(Hat2)  

print(Mug1)  
print(Mug2)  
