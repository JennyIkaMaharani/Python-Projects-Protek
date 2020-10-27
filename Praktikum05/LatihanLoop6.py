#Game
from random import randint
bil = randint(0,100)
nilai= 100
print(bil)
print("Hai.. nama saya Mr. Lappie. Saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
tebak = int(input("Tebakan Anda :"))
while(tebak != bil):
    if(tebak <= bil):
        print("Hehehe... Bilangan tebakan Anda terlalu kecil")
    elif(tebak>= bil):
        print("Hehehe... Bilangan tebakan Anda terlalu besar")
    nilai = nilai - 2
    tebak = int(input("Tebakan Anda :"))
if(nilai<=0):
    nilai = 0
print("Yeeee... Bilangan tebakan Anda BENAR")
print("Score Anda :", nilai)
