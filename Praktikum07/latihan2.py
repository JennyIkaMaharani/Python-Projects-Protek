# input nama file
namaFile = input('Masukkan nama file : ')

try:
    file = open (namaFile, "r") #membuka dan membaca file
    file = open (namaFile, "a") 
    tambahan = input('Data yang mau ditambahkan: ')
    file.write(tambahan)
    tambah = input('Mau lagi (y/n): ')
    while tambah == 'y':
        tambahan = input('Data yang mau ditambahkan: ')
        file.write(tambahan)
        tambah = input('Mau lagi (y/n): ')
    file.close()
except FileNotFoundError:
	print('Maaf file tidak ditemukan')
