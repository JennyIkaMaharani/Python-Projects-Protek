#program mencari mahasiswa dengan nilai akhir terbaik
def theBest(data):
    rekap = [] #membuat list kosong
    for a in range(len(data)):
        list = nilaiMhs[a] #mengambil data tiap mahasiswa
        nilaiAkhir = (list['mid'] + 2*list['uas']) / 3 #menghitung nilai akhir tiap mahasiswa
        rekap.append(nilaiAkhir) #menambah nilai akhir ke dalam list rekap
    best = rekap.index(max(rekap)) #mencari index dari nilai tertinggi
    where = data[best] #mencari dictionary mahasiswa nilai tertinggi
    who = where['nama'] + " " + where['nim']
    return who
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

print(theBest(nilaiMhs))
