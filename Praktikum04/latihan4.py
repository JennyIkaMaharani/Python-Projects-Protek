#menghitung waktu tiba Pak Amir di kota C
#jarak A-B = 125km dengan kecepatan 62km/jam
#jarak B-C + 256km dengan kecepatan 70km/jam
#berangkat pukul 06.00 dan beristirahat selama 45 menit
jarakAB=125
kecepatanAB=62
jarakBC=256
kecepatanBC=70
menitBerangkat=0
jamBerangkat=6
lamaJam=jarakAB//62+jarakBC//70
lamaMenit=round(jarakAB%kecepatanAB/62*60+jarakBC%kecepatanBC/70*60)
menitTiba=((lamaMenit+45)//60)+((lamaMenit+45)%60/100)
jamTiba=lamaJam+jamBerangkat
waktuTiba=jamTiba+menitTiba
print(waktuTiba)
