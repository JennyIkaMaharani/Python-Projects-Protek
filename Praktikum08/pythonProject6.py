#mendefinisikan function
def sortStringByChar(y):
    hasil = []
    banyak = len(y) - 1
    panjang = len(y[0])
    for data in range (banyak):
        x = len(y)-1
        i = 0
        #membandingkan panjang karater tiap data dalam list
        while i < x:
            if len(y[i]) > len(y[i+1]):
                besar= y[i]
                kecil = y[i+1]
            elif len(y[i]) < len(y[i+1]):
                besar = y[i+1]
                kecil = y[i]
            i += 1
        hasil.append(kecil) #menambahkan data terpendek ke list hasil
        y.remove(kecil) #menghapus data terpendek
    hasil.insert(0, besar) #menambahkan data terpanjang ke index ke-0
    return hasil
    
myData = ['apel', 'rambutan', 'jeruk ']
print(sortStringByChar(myData))
