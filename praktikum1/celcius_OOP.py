print ("Nama 	: Adjie Priyanto")
print ("NIM 	: 221511006")
print ("Kelas 	: K2 Teknik Informatika")
print ()

class suhu:
	def __init__(self, celcius):
		self._celcius = celcius
		
	def get_fahrenhait(self):
		return (9*self._celcius/5) + 32
		
	def get_kelvin(self):
		return self._celcius + 273
		
	def get_reamur(self):
		return (4/5) * self._celcius
		
c = suhu(10)

print (" ----------------- Konversi Celcius ----------------- ")
print ("")
print("konversi Celcius ke Fahrenhait : ",c.get_fahrenhait(), "derajat Fahrenhait")
print("konversi Celcius ke Kelvin : ",c.get_kelvin(), "derajat Kelvin")
print("konversi Celcius ke Reamur : ",c.get_reamur(), "derajat Reamur")
