#program pembaca input nim, nama, dan alamat
#program penyimpan input ke file dan penampil data

#membuka file
file = open('d:\myFile.txt', 'w')
#menerima input
lagi = 'y'
while lagi == 'y':
    nim = input('Masukkan NIM          : ')
    nama = input('Masukkan Nama Mhs     : ')
    alamat = input('Masukkan Alamat       : ')
    dataAwal = [nim, nama, alamat]
    #menggabung data
    data = '|'.join(dataAwal) + '\n'
    #menulis data pada file
    file.write(data)
    lagi = input('Ulangi input lagi(y/n): ')
file.close()
file = open('d:\myFile.txt', 'r')
hasil = file.read()
print(hasil)
file.close()
