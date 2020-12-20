#membuat program bintang
#mendedinisikan function
def bintang(n):
    j = 1
    k = 1 + 2*(n)
    for i in range(n):
        a = "*" * j
        #menampilkan karakter di bagian tengah
        print(a.center(k))
        j +=2
bintang(4)