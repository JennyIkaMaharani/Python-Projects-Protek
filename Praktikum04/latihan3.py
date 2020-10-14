#menentukan berapa kali Pak Budi mengisi bensin
#jika kapasitas tangki 50 liter
#berdasarkan info dari latihan 2
import math
#latihan2
jarak=795
bensin=jarak//12+jarak%12/12
#menghitung berapa kali mengisi bensin
kapasitas=50
mengisi= math.ceil(bensin/kapasitas)
print(mengisi, end=" kali")
