#membuat program menghitung rata-rata harga buah
buah = {'apel' : 5000, 
    'jeruk' : 8500, 
    'mangga' : 7800, 
    'duku' : 6500}
harga = list(buah.values()) #ini membuat list harga dari value
#menghitung rata rata
rataRata= sum(harga) / len(harga)
print(rataRata)