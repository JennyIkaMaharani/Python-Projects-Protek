def faktorial(n):
  jum = 1
  for i in range (2, (n+1)):
      jum *= i
  return jum
# C(5,3)
com = faktorial(5) / faktorial (3) / faktorial((5-3))
print('Hasil C(5,3) adalah ', com)
#P(10,7)
per = faktorial(10) / faktorial((10-7))
print('Hasil P(10,7) adalah ', per)
