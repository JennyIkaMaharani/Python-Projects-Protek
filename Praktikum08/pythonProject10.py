#membuat program menghitung total harga yang harus dibayar
buah = {'apel' : 5000, 
    'jeruk' : 8500, 
    'mangga' : 7800, 
    'duku' : 6500}
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