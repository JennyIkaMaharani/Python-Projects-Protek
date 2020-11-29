#input nama mahasiswa
n = int(input('Banyak nama mahasiswa: '))
nama = []
karakter = []
for i in range (n):
    who = input('Nama mahasiswa: ')
    nama = nama + [who]
    nama.sort()
for data in range (len(nama)):
    name = nama[data]
    char = len(nama[data])
    print(name, '(', char, "karakter)'")
