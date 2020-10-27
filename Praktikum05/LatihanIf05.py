#Menentukan gaji pokok dan gaji bersih
kode = input("Masukkan kode karyawan                 : ")
nama = input("Masukkan nama karyawan                 : ")
golongan = input("Masukkan golongan                      : ")
status= input("Masukkan status (1= menikah, 2= belum) : ")
if(status=="1"):
    anak= input("Masukkan jumlah anak                   : ")
else:
    anak = 0
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
jumAnak=int(anak)
if(jumAnak >=0):
    tunAnak = int(5/100*gaji*jumAnak)
if(status=="1"):
    tunNikah=int(10/100*gaji)
    gajiKotor= gaji + tunNikah + tunAnak
if(status == "2"):
    tunNikah = 0
    gajiKotor = gaji
potong= int(pot/100*gajiKotor)
gajiBersih= gajiKotor - potong
print(" ")
print("==========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------------")
print("Nama Karyawan     :", nama, "(Kode:", kode, ")")
print("Golongan          :", golongan)
print("Status Menikah    :", status)
print("Jumlah Anak       :", jumAnak)
print("------------------------------------------")
print("Gaji Pokok            :", "Rp", gaji)
print("Tunjangan istri/suami :", "Rp ", tunNikah)
print("Tunjangan anak        :", "Rp ", tunAnak)
print("---------------------------------------- +")
print("Gaji kotor            :", "Rp", gajiKotor)
print("Potongan (", pot, "%)     :", "Rp  ", potong)
print("---------------------------------------- -")
print("Gaji Bersih           :", "Rp", gajiBersih)
