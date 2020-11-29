#program menambah, menghapus, dan menampilkan data sayur
sayur = ['bayam', 'kangkung', 'wortel', 'selada'] #menampilkan list

#menampilkan menu
print('Menu: ') 
print('A. Tambah data sayuran')
print('B. Hapus data sayuran')
print('C. Tampilkan data sayuran')
#memasukkan pilihan
pilih = input('Pilihan Anda: ')
while True:
    try:
        if pilih == 'A' or pilih == 'a':
            tambah = input('Tambahan sayur:') #input data tambahan
            sayur.append(tambah) #menambah data dalam list
        elif pilih == 'B' or pilih == 'b':
            hapus = input('Sayuran yang dihapus:') #input data yang ingin dihapus
            sayur.remove(hapus) #menghapus data
        elif pilih == 'C' or pilih == 'c':
            for veg in range(len(sayur)):
                print(str(sayur[veg]), end=" ")
            print () #menampilkan list sayuran
        pilih = input('Pilihan Anda: ')
    except ValueError: #mencegah exception
        print('Data tidak ditemukan')
        break
