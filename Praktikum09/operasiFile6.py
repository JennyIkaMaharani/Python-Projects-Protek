#membuat tabel dari data
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print('=' * 72)
print('NIM'.ljust(12), end='')
print('NAMA'.ljust(12), end='')
print('N. MID'.rjust(8), end='')
print('N. UAS'.rjust(12), end='')
print('N. AKHIR'.rjust(12), end='')
print('STATUS'.rjust(15))
print('-' * 72)
for i in range(len(nilai)):
    data = nilai[i]
    nim = data['nim']
    nama = data['nama']
    mid = data['mid']
    uas = data['uas']
    akhir = (mid + 2*uas)/3
    if akhir >= 60 :
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
    print(str(nim).ljust(12), end='')
    print(str(nama).ljust(12),end='')
    print(str(mid).rjust(8), end='')
    print(str(uas).rjust(12), end='')
    print(str(round(akhir)).rjust(12),end='')
    print(status.rjust(15))
    
print('-' * 72)
