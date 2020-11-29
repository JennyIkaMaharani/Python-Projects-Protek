#membuat fungsi kuadrat
def kuadrat(bil):
    hasil = []
    for data in range (len(bil)):
        result = bil[data]**2 #mengkuadratkan setiap data di list 
        hasil = hasil + [result] #membuat list hasil
    return hasil #mengembalikan hasil proses
    
bil = [2, 3, 4, 5, 6]
print(kuadrat(bil))