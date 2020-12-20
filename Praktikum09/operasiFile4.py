#membuat function untuk mengacak string
#mengimport random
import random
def shuffleString(x,n):
    #mengubah string ke list
    kata = list(x)
    #membuat list kosong
    listHasil = []
    listHasil1 = []
    while True:
        #mengacak huruf
        random.shuffle(kata)
        #menggabung huruf menjadi kata
        hasil = "".join(kata)
        #mengecek keberadaan kata di list
        a = hasil in listHasil1
        if a == False:
            listHasil1 = listHasil1 + [hasil]
        if len(listHasil1)== n :
            listHasil = listHasil1
            break
    return listHasil
print(shuffleString('aku',2))
print(shuffleString('aku',3))
print(shuffleString('aku',4))
