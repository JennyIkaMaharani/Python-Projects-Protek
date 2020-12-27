#input berupa file dan nilai n
#membuka file
sandi = open('d:\encryptedFile.txt', 'r')
n = int(input('Masukkan nilai n: '))
#membaca isi file
char = sandi.read()
#mengubah isi ke bentuk data list
huruf = list(char)
#membuat list kosong untuk hasil
terbaca = []
#menerjemahkan sandi
for i in huruf:
    #mengubah karakter ke nilai ASCII
    ascii1 = ord(i)
    if ascii1 == 32:
        ascii2 = ascii1
    else:
        #menggeser huruf ke bentuk asal
        ascii2 = ascii1 - n
        if ascii2 < 65:
            ascii2 = ascii2 + 26
        elif (90 < ascii2 and ascii2 <97):
            ascii2 = ascii2 + 26
    #mengubah nilai ASCII ke huruf
    terj = chr(ascii2)
    #menambahkan huruf ke list
    terbaca.append(terj)
#menggabngkan data dalam list hasil
terjemahan = ''.join(terbaca)
#membuka file hasil
hasil = open('d:\hasil.txt', 'w')
#menuliskan terjemahan ke file tujuan
hasil.write(terjemahan)
#menutup file
hasil.close()
sandi.close()
