print ("Nama 	: Adjie Priyanto")
print ("NIM 	: 221511006")
print ("Kelas 	: K2 Teknik Informatika")
print ()

class suhu:
	def __init__(self, Reamur):
		self._Reamur = Reamur
		
	def get_celcius(self):
		return 5/4 * self._Reamur
		
	def get_fahrenhait(self):
		return 9/4 * self._Reamur + 32
		
	def get_kelvin(self):
		return 5/4 * self._Reamur + 273
		
r = suhu(10)

print (" ----------------- Konversi Reamur ----------------- ")
print ("")
print("konversi Reamur ke Celcius : ",r.get_celcius(), "derajat Celcius")
print("konversi Reamur ke Fahrenhait : ",r.get_fahrenhait(), "derajat Fahrenhait")
print("konversi Reamur ke Kelvin : ",r.get_kelvin(), "derajat Kelvin")
