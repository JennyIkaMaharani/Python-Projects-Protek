#membuat program mengubah huruf
def ubahHuruf(teks, a, b):
    #mengubah teks menjadi list
    listHuruf= list(teks)
    baru = []
    for i in range (len(listHuruf)):
        huruf = listHuruf[i]
        #mengganti huruf
        if huruf == a:
            huruf = b
        baru = baru + [huruf]
    #menggabungkan list
    hasil= "".join(baru)
    return hasil
y = ubahHuruf('MATEMATIKA', 'T', 'S')
print(y)
