#Menentukan gaji pokok dan gaji bersih
kode = input("Masukkan kode karyawan                 : ")
nama = input("Masukkan nama karyawan                 : ")
golongan = input("Masukkan golongan                      : ")
if(golongan == "A") or (golongan == "a"):
    gaji = 10000000
    pot = 2.5
elif(golongan == "B") or (golongan == "b"):
    gaji = 8500000
    pot = 2.0
elif(golongan == "C") or (golongan == "c"):
    gaji = 7000000
    pot = 1.5
elif(golongan == "D") or (golongan == "d"):
    gaji = 5500000
    pot= 1.0
potong = int(pot/100*gaji)
gajiBersih= gaji-potong
print(" ")
print("===================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------")
print("Nama Karyawan     :", nama, "(Kode:", kode, ")")
print("Golongan          :", golongan)
print("-----------------------------------")
print("Gaji Pokok        :", "Rp", gaji)
print("Potongan (", pot, "%) :", "Rp  ", potong)
print("--------------------------------- -")
print("Gaji Bersih       :", "Rp", gajiBersih)

