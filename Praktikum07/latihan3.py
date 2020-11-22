#menampilkan judul
print('------------------------------------------')
print('        PROGRAM HITUNG RATA-RATA          ')
print('------------------------------------------')
jumlah = 0
data = 0
lanjut = 'y'
while lanjut == 'y':
    try:
        angka = int(input('Masukkan bilangan bulat: '))
    except ValueError:
        print('Bukan bilangan bulat')
        angka = int(input('Masukkan bilangan bulat: '))
    jumlah += angka
    data += 1
    lanjut = input('Lagi (y/n)? :')
    if lanjut == 'n':
        mean = jumlah/data
        break
print('Rata-ratanya adalah ', mean)
