from datetime import *
pinjam = datetime.date(datetime.now())
kembali = pinjam + timedelta(days = 7)
file = open('d:\dataPeminjaman.txt', 'w')
lanjut = 'y'
while lanjut == 'y':
    kode = input('Masukkan Kode Member   : ')
    nama = input('Masukkan Nama Member   : ')
    judul = input('Masukkan Judul Buku    : ')
    listData = [kode.upper(), nama, judul, str(pinjam), str(kembali)]
    data = '|'.join(listData) + '\n'
    file.write(data)
    lanjut = input('Ulangi lagi (y/n)      : ')
    if lanjut == 'n':
        break
    
file.close()
