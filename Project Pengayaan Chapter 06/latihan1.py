def isPrime(x):
    i = x-1
    jum=0
    while (i>1):
        bagi = x % i
        if (bagi == 0):
            jum+=1
            break
        i -= 1
    if(jum != 0):
        print("Kesimpulan:", x, "Bukan Prima")
    else:
        print("Kesimpulan:", x, "Prima")
a=7
isPrime(a)
b=8
isPrime(b)
