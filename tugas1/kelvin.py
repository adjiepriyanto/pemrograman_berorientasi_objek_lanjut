print ("Nama 	: Adjie Priyanto")
print ("NIM 	: 221511006")
print ("Kelas 	: K2 Teknik Informatika")
print ()

class suhu:
	def __init__(self, kelvin):
		self._kelvin = kelvin
		
	def get_celcius(self):
		return self._kelvin - 273

		
	def get_reamur(self):
		return 4/5 * (self._kelvin - 273)
		
k = suhu(10)

print (" ----------------- Konversi Kelvin ----------------- ")
print ("")
print("konversi Kelvin ke Celcius : ",k.get_celcius(), "derajat Celcius")
print("konversi Kelvin ke Reamur : ",k.get_reamur(), "derajat Reamur")
