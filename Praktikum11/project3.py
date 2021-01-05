from project1 import diffDate
from datetime import *
kode = input('Masukkan Kode Member     : ')
file = open('d:\dataPeminjaman.txt', 'r')
baca = file.readlines()
for i in range(len(baca)):
    data = baca[i]
    data.replace('\n','')
    dataPinjam = data.split('|')
    if kode.upper() == dataPinjam[0]:
        nama = dataPinjam[1]
        judul = dataPinjam[2]
        pinjam = dataPinjam[3]
        y, m, d = (dataPinjam[4]).split('-')
        maksKembali = date(int(y), int(m), int(d))
        kembali = datetime.date(datetime.now())
        selisih = kembali - maksKembali
        selisihHari = selisih.days
        if selisihHari < 0:
            selisihHari = 0
        if selisihHari > 0:
            denda = selisihHari * 2000
        else:
            denda = 0
        print('Data Peminjaman Buku')
        print('Kode Member              : ', kode.upper())
        print('Nama Member              : ', nama)
        print('Judul Buku               : ', judul)
        print('Tanggal Mulai Peminjaman : ', pinjam)
        print('Tanggal Maks peminjaman  : ', maksKembali)
        print('Tanggal Pengembalian     : ', kembali)
        print('Terlambat                : ', selisihHari, 'hari')
        print('Denda                    : ', 'Rp', denda)
        break
    else :
        data = 'none'
if data == 'none':
    print('Maaf data tidak ditemukan')
