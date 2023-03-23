print ("Nama 	: Adjie Priyanto")
print ("NIM 	: 221511006")
print ("Kelas 	: K2 Teknik Informatika")
print ()
print (" ----------------- Konversi Celcius ----------------- ")
print ("")

def suhu(c):
	fahrenhait = (9 * c /5)+32
	print ("Konversi Celcius ke Fahrenhait : ", fahrenhait, "derajat Fahrenhait")
	
	kelvin = c + 273
	print ("Konversi Celcius ke Kelvin : ", kelvin, "derajat Kelvin")
	
	reamur = (4 / 5) * c
	print ("Konversi Celcius ke Reamur : ", reamur, "derajat Reamur")
	
suhu(10)

