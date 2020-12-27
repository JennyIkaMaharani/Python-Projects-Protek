#membuka file
file= open('d:\myFile.txt', 'r')
#membaca file per baris
data = file.readlines()
#membuat dictionary kosong
dataMahasiswa = {}

for i in range(len(data)):
    mhs = data[i]
    #memisah data
    nim, nama, alamat = mhs.split('|')
    #membuat dictionary
    dataMhs = {'nim': nim, 'nama': nama, 'alamat': alamat}
    dataMahasiswa[nama] = dataMhs
print(dataMahasiswa)
#menutup file
file.close()
