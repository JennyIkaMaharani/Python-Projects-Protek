#program penyandian file
#menerima input berupa nama file dan n
nama = input("Masukkan nama file: ")
n = int(input('Masukkan nilai n  : '))
#membuka file
asli = open(nama, 'r')
#membaca isi file
char = asli.read()
#mengubah data dari file menjadi list
huruf = list(char)
#membuat list kosong
tersandi = []
for i in huruf:
    #mengubah karakter ke nilai ASCII
    ascii1 = ord(i)
    #tidak mengubah karakter spasi
    if ascii1 == 32:
        ascii2 = ascii1
    else:
        #menambahkan n ke nilai ASCII agar huruf bergeser
        ascii2 = ascii1 + n
        if ascii2 > 122:
            ascii2 = ascii2 - 26
        elif ascii2 > 90 and ascii2 <97 :
            ascii2 = ascii2 - 26
    sandi = chr(ascii2)
    tersandi = tersandi +[sandi]
    if not huruf:
        break
#menggabung karakter yang telah disandi
encrypted = ''.join(tersandi)
#menulis hasil penyandian ke file baru
hasil = open('d:\encryptedFile.txt', 'w')
hasil.write(encrypted)
hasil.close()
