#Menentukan kelulusan mahasiswa
nBhs= int(input("Masukkan nilai Bahasa Indonesia : "))
nMtk= int(input("Masukan nilai Matematika        : "))
nIpa= int(input("Masukkan nilai IPA              : "))
if(nBhs <= 100) and (nMtk <= 100) and (nIpa <=100):
    if(nBhs >=0) and (nMtk >=0) and (nIpa >=0):
        if(nBhs >=60) and (nMtk >= 70) and (nIpa >= 60):
            status = "LULUS"
        else:
            status = "TIDAK LULUS"
print("Status Kelulusan                :", status)

