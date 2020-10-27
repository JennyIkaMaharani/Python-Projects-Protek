#kotak bintang ajaib
baris=5
kolom=5

i = 5
while(baris >= 0):
    j = i
    while (j > 0):
        print("*", end="")
        j -= 1 
    i -= 1
    print("")
    if(i < 0):
        break
