#pastikan modul playsound sudah terinstall
from playsound import playsound

class Hewan:
    suara = "gaada.mp3"

    def mainkan_suara(self):
        playsound(self.suara)

class CanadianFlock(Hewan):
    suara = "CanadianFlock.mp3"

class CanaryTrills(Hewan):
    suara = "CanaryTrills.mp3"

class CrowCaw(Hewan):
    suara = "CrowCaw.mp3"

class MeadowLark(Hewan):
    suara = "MeadowLark.mp3"

class MexicanRedParot(Hewan):
    suara = "MexicanRedParot.mp3"

class MockingbirdCry(Hewan):
    suara = "MockingbirdCry.mp3"

class Peacock(Hewan):
    suara = "Peacock.mp3"

class Vulture(Hewan):
    suara = "Vulture.mp3"

class Whipperwhill(Hewan):
    suara = "Whipperwhill.mp3"

class Woodpecker(Hewan):
    suara = "Woodpecker.mp3"

#instansiasi
CanadianFlock=CanadianFlock()
CanaryTrills=CanaryTrills()
CrowCaw=CrowCaw() 
MeadowLark=MeadowLark()
MexicanRedParot=MexicanRedParot()
MockingbirdCry=MockingbirdCry()
Peacock=Peacock()
Vulture=Vulture()
Whipperwhill=Whipperwhill()
Woodpecker=Woodpecker()

#contoh pemanggilan
CanadianFlock.mainkan_suara()
CanaryTrills.mainkan_suara()
CrowCaw.mainkan_suara()
MeadowLark.mainkan_suara()
MexicanRedParot.mainkan_suara()
MockingbirdCry.mainkan_suara()
Peacock.mainkan_suara()
Vulture.mainkan_suara()
Whipperwhill.mainkan_suara()
Woodpecker.mainkan_suara()

#apa bila terjadi error coba upgrade/downgrade ke module playsound versi 1.2.2


