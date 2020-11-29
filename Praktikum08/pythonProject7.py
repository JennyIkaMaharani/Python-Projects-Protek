#membuat function untuk menentukan buah termahal
def manaTermahal(buah):
    jenis = list(buah.keys()) #membuat list jenis buah
    harga = list(buah.values()) #membuat list harga buah
    most = max(harga) #mencari nilai paling besar dari list harga
    y = harga.index(most) #mencari index dari harga terbesar
    termahal = jenis[y] #mencari nilai dari index harga terbesar
    print(termahal) #menampilkan nama buah
buah = {'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500 }
manaTermahal(buah)
