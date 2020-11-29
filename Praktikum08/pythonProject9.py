#membuat program menentukan harga yang harus dibayar
buah = {'apel' : 5000, 
    'jeruk' : 8500, 
    'mangga' : 7800, 
    'duku' : 6500}
#membuat list
jenis = list(buah) 
harga = list(buah.values())
namaBuah = input("Nama buah yang dibeli: ") #memasukkan nama buah
kgBuah = int(input("Berapa kg                        : ")) #memasukkan jumlah buah dalam kg
print("-------------------------------------------")
indeks = jenis.index(namaBuah) #mencari index dari nama buah dalam list
total = harga[indeks] * kgBuah #menghitung total harga
print("Total harga                     : ", total)