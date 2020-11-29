#menampilkan menu
print("Menu:")
print("A. Tambah data")
print("B. Beli buah")
print("C. Hapus buah")
buah = {'apel' : 5000, 
    'jeruk' : 8500, 
    'mangga' : 7800, 
    'duku' : 6500}
pilih = input("Pilihan Menu : ") #menerima pilihan
if pilih == "a" :
    nama = input("Masukkan nama buah    : ") #menerima masukkan nama
    harga = int(input("Masukkan harga satuan : ")) #menerima masukkan harga
    ada = nama in buah.keys() #mengecek eksistensi nama dalam list buah
    if ada == True:
        print("Nama buah sudah ada")
    else:
        buah[nama] = harga #menambah data pada dictionary
    print("Data buah: ")
    for x, y in buah.items() :
        print("-", x, "(Harga Rp", y, ")")
elif pilih == "b":
    #membuat list
    jenis = list(buah) 
    harga = list(buah.values())
    tambah = 'y'
    total = 0
    while True:
        namaBuah = input("Nama buah yang dibeli: ") #memasukkan nama buah
        kgBuah = int(input("Berapa kg                        : ")) #memasukkan jumlah buah dalam kg
        indeks = jenis.index(namaBuah) #mencari index dari nama buah dalam list
        totalSementara = harga[indeks] * kgBuah #menghitung total harga tiap item
        total = total + totalSementara #menghitung total keseluruhan
        tambah = input("Ingin beli buah yang lain(y/n)? ")
        if tambah == "n":
            break
    print("-------------------------------------------")
    print("Total harga                     : ", total)
elif pilih == "c" :
    hapus = input("Masukkan nama buah: ") #menerima masukkan nama buah yang dihapus
    ada = hapus in buah.keys() #mengecek eksistensi nama dalam dictionary
    if ada == True:
        del buah[hapus] #menghaous data
    elif ada == False:
        print("Nama buah tidak ditemukan")