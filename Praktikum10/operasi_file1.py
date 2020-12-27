#program membaca dan menampilkan jumlah bilangan genap dan ganjil
#membuka file
file = open('d:\data.txt','r')
#membaca file
angka = file.readlines()
# menghitung jumlah angka genap dan ganjil
genap=[]
ganjil=[]
for i in range(len(angka)):
    num = angka[i]
    if (int(num)%2) == 0 :
        genap = genap + [num]
    else :
        ganjil = ganjil + [num]
print('Banyaknya bilangan genap : ', len(genap))
print('Banyaknya bilangan ganjil: ', len(ganjil))
