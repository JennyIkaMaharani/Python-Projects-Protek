#menghitung tarif sewa mobil dari 06.00 sampai 23.50
#dengan tarif Rp200.000 untuk 12 jam pertama
#dan Rp10.000 per jam untuk berikutnya

jamPinjam=6
menitPinjam=00
jamKembali=23
menitKembali=50
lamaJam=jamKembali-jamPinjam
lamaMenit=menitKembali-menitPinjam
#12 jam pertama
tarif1=lamaJam//12*200000
#setelah 12 jam
tarif2=lamaJam%12*10000+lamaMenit//60*10000

totalBiaya=tarif1+tarif2
print(totalBiaya)
