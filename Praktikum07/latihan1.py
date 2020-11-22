# input nama file
namaFile = input("Masukkan nama file : ")

try:
    file = open (namaFile, "r") #membuka dan membaca file
    print('Isi dari file', namaFile, 'adalah ')
    print(file.read()) #menampilkan isi file
except FileNotFoundError:
	print('Maaf file tidak ditemukan')
