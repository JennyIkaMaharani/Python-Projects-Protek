#membuat program bintang
#mendedinisikan function
def bintang(n):
    #membagi jumlah baris
    x = n//2
    y = n - x
    j = 1
    k = 1 + (x-1)*2
    l = 1 + x*2
    #menampilkan piramida bintang atas
    for i in range(y):
        a = "*" * j
        print(a.center(l))
        j +=2
    #menampilkan piramida bintang bawah
    for i in range(x):
        b = "*" * k
        print(b.center(l))
        k -= 2
bintang(7)
