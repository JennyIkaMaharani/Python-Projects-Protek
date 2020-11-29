#membuat list (langkah 1)
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print (b)
#menyisipkan nilai (langkah 2)
a.insert(3, 10)
b.insert(2, 15)
print(a)
print (b)
#menyisipkan nilai ke indeks paling akhir
a.append(4)
b.append(8)
print(a)
print (b)
#melakukan sorting secara ascending
a.sort()
b.sort()
print(a)
print (b)
#membuat sublist
c = a[:8]
d = b[2:10]
print(c)
print (d)
#langkah 6
e = []
for i in range(len(c)):
    data = c[i] + d[i]
    e = e + [data]
print(e)
#mengubah list ke tuple
e = tuple(e)
print(e)
#mencari nilai min, max, dan jumlah
print(min(e)) #menampilkan nilai terkecil
print(max(e)) #menampilkan nilai terbesar
print(sum(e)) #menampilkan jumlah data

#membuat string
myString = "python adalah bahasa pemrograman yang menyenangkan"
huruf = set(myString)
print(huruf)
listHuruf = list(huruf)
listHuruf.sort()
print(listHuruf)
