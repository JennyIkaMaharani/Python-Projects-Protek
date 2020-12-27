#membuat program penjumlah data dari file kemudian menuliskannya pada file baru
#membuka file asal
asal = open('d:\data2.txt', 'r')
#membuka file tujuan
tujuan = open('d:\hasil.txt', 'w')
#membaca isi file asal
data = asal.readlines()

for i in range(len(data)):
    bil = data[i]
    #memisahkan data
    bilA, bilB = bil.split('|')
    #menjumlah dua bilangan
    bilC = int(bilA) + int(bilB)
    bil3 = str(bilC)
    #menuliskan hasil pada file baru
    tujuan.write(bil3)
    tujuan.write('\n')
tujuan.close()
hasil = open('d:\hasil.txt', 'r')
print(hasil.read())
hasil.close
