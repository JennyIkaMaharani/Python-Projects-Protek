#Menampilkan bilangan ganjil dari 0-100
sum=0
for i in range (100):
    bil= i + 1
    if (bil % 2 != 0):
        print(bil)
        sum = sum + 1
print("Banyaknya bilangan ganjil :", str(sum))
