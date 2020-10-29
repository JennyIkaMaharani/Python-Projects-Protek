def luasSegitiga2(a,t):
    luas = a * t / 2
    return luas
alas1 = 10
tinggi1 = 20
print('Luas segitiga dg alas ', alas1,
      ' dan tinggi ', tinggi1,
      ' adalah ', luasSegitiga2(alas1,tinggi1))
alas2 = 15
tinggi2 = 45
print('Luas segitiga dg alas ', alas2,
      ' dan tinggi ', tinggi2,
      ' adalah ', luasSegitiga2(alas2,tinggi2))
luasTotal= luasSegitiga2(alas1, tinggi1) + luasSegitiga2(alas2, tinggi2)
print('Luas total dua segitiga adalah ', luasTotal)
