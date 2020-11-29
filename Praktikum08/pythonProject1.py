#menentukan jumlah bilangan
n = int(input('Masukkan nilai n:'))
bil = []
for i in range(n):
    angka = int(input('Masukkan data: '))
    bil = bil + [angka]
bil.sort(reverse=True)
print(bil)
