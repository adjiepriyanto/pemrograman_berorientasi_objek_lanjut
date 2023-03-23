print ("Nama 	: Adjie Priyanto")
print ("NIM 	: 221511006")
print ("Kelas 	: K2 Teknik Informatika")
print ()

class suhu:
	def __init__(self, fahrenhait):
		self._fahrenhait = fahrenhait
		
	def get_celcius(self):
		return (self._fahrenhait - 32) * 5/9
		
	def get_kelvin(self):
		return (self._fahrenhait - 32) * 5/9 + 273
		
	def get_reamur(self):
		return 4/9 * 4 * (self._fahrenhait - 32)
		
f = suhu(10)

print (" ----------------- Konversi Fahrenhait ----------------- ")
print ("")
print("konversi Fahrenhait ke Celcius : ",f.get_celcius(), "derajat Celcius")
print("konversi Fahrenhait ke Kelvin : ",f.get_kelvin(), "derajat Kelvin")
print("konversi Fahrenhait ke Reamur : ",f.get_reamur(), "derajat Reamur")
