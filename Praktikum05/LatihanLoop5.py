#Game
from random import randint
bil = randint(0,100)
print(bil)
print("Hai.. nama saya Mr. Lappie. Saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
tebak = int(input("Tebakan Anda :"))
while(tebak != bil):
    if(tebak <= bil):
        print("Hehehe... Bilangan tebakan Anda terlalu kecil")
    elif(tebak>= bil):
        print("Hehehe... Bilangan tebakan Anda terlalu besar")
    tebak = int(input("Tebakan Anda :"))
print("Yeeee... Bilangan tebakan Anda BENAR")
