from operation import*
print('a. 2 + 4 * 6 – 4 = ', jumlah(kurang(kali(4,6), 4), 2))
print('b.(4 + 7) * (6 - 9) =', kali(jumlah(4,6), kurang(6,9)))
x = jumlah(4,7)
y = jumlah(7,5)
z = kurang(12,34)
print('c.(10 + 2) / (7 + 5) / (12 - 34) =', bagi(bagi(x,y), z))
