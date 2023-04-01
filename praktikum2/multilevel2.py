class hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def berbunyi(self):
        pass
    
class mamalia(hewan):
    def __init__(self, nama):
        super().__init__(nama)
    
    def melahirkan(self):
        pass
    
class harimau (mamalia):
    def __init__(self, nama):
        super().__init__(nama)
    
    def berbunyi(self):
        return "rawr"
    
class ayam(mamalia):
    def __init__(self, nama):
        super().__init__(nama)
    
    def berbunyi(self):
        return "kukuruyuk"
    
class burung(hewan):
    def __init__(self, nama):
        super().__init__(nama)
    
    def fly(self):
        pass
    
class deruk(burung):
    def __init__(self, nama):
        super().__init__(nama)
    
    def berbunyi(self):
        return "kukderukuk"
    
harimauA = harimau("bily")
ayamA = ayam("jalu")
derukA = deruk("jimi")

print(harimauA.nama + ": " + harimauA.berbunyi())
print(ayamA.nama + ": " + ayamA.berbunyi())
print(derukA.nama + ": " + derukA.berbunyi())
