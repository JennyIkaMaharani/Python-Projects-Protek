#program pencari data berdasarkan NIM
#menerima input berupa NIM
find = input('Massukkan NIM yang mau dicari: ')
#membuka file dan membaca data
file = open('d:\myFile.txt', 'r')
isi = file.readlines()
for i in range(len(isi)):
    mhs = isi[i]
    nim, nama, alamat = mhs.split('|')
    if nim == find :
        data = 'ada'
        #menampilkan data
        print('Data Mahasiswa')
        print('NIM    : ', nim)
        print('Nama   : ', nama)
        print('Alamat : ', alamat)
        break
    else:
        data = 'none'
#menampilkan 'data tidak ditemukan' ketika data tidak ada
if data == 'none':
    print('Data mahasiswa tidak ditemukan')
