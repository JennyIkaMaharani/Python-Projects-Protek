#mengimport datetime
from datetime import *
#mendefinisikan function
def diffDate(x):
    today = datetime.date(datetime.now())
    y, m, d = x.split('-')
    tglCari = date(int(y), int(m), int(d))
    selisih = today - tglCari
    selisihHari= abs(selisih.days)
    return selisihHari

