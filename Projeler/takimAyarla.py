class Futbolcu:
    def __init__(self, ad, forvet_ozellikler, ortasaha_ozellikler, defans_ozellikler):
        self.ad = ad
        self.forvet = forvet_ozellikler
        self.ortasaha = ortasaha_ozellikler
        self.defans = defans_ozellikler
    
    def forvet_bilgisi(self):
        return f"Forvet Özellikleri (Hız: {self.forvet['hiz']}, Şut: {self.forvet['sut']}, Top Kontrolü: {self.forvet['top_kontrol']})"
    
    def ortasaha_bilgisi(self):
        return f"Orta Saha Özellikleri (Pas: {self.ortasaha['pas']}, Vizyon: {self.ortasaha['vizyon']}, Top Kontrolü: {self.ortasaha['top_kontrol']})"
    
    def defans_bilgisi(self):
        return f"Defans Özellikleri (Savunma: {self.defans['savunma']}, Top Kapma: {self.defans['top_kapma']}, Pozisyon: {self.defans['pozisyon']})"
    
    def toplam_puan(self):
        toplam = (sum(self.forvet.values()) + sum(self.ortasaha.values()) + sum(self.defans.values())) / 9
        return toplam


def showBilgi(x):
    print(f"Futbolcu Adi: {x.ad}")
    print(x.forvet_bilgisi())
    print(x.ortasaha_bilgisi())
    print(x.defans_bilgisi())
    print(f"Toplam Puan: {x.toplam_puan()}\n")


# Futbolcular
futbolcular = [
    Futbolcu("Aras", {"hiz": 80, "sut": 80, "top_kontrol": 77}, {"pas": 78, "vizyon": 82, "top_kontrol": 80}, {"savunma": 73, "top_kapma": 75, "pozisyon": 74}),
    Futbolcu("Berat", {"hiz": 82, "sut": 85, "top_kontrol": 80}, {"pas": 84, "vizyon": 85, "top_kontrol": 83}, {"savunma": 72, "top_kapma": 73, "pozisyon": 74}),
    Futbolcu("Eren", {"hiz": 85, "sut": 85, "top_kontrol": 80}, {"pas": 84, "vizyon": 83, "top_kontrol": 83}, {"savunma": 75, "top_kapma": 74, "pozisyon": 75}),
    Futbolcu("Boran", {"hiz": 77, "sut": 73, "top_kontrol": 77}, {"pas": 79, "vizyon": 80, "top_kontrol": 79}, {"savunma": 70, "top_kapma": 72, "pozisyon": 74}),
    Futbolcu("Mustafa", {"hiz": 71, "sut": 70, "top_kontrol": 69}, {"pas": 73, "vizyon": 77, "top_kontrol": 70}, {"savunma": 77, "top_kapma": 71, "pozisyon": 70}),
    Futbolcu("Murat", {"hiz": 81, "sut": 73, "top_kontrol": 68}, {"pas": 71, "vizyon": 76, "top_kontrol": 67}, {"savunma": 79, "top_kapma": 79, "pozisyon": 80}),
    Futbolcu("Mami", {"hiz": 83, "sut": 81, "top_kontrol": 74}, {"pas": 79, "vizyon": 83, "top_kontrol": 74}, {"savunma": 73, "top_kapma": 72, "pozisyon": 74}),
    Futbolcu("Bilal", {"hiz": 80, "sut": 82, "top_kontrol": 80}, {"pas": 84, "vizyon": 82, "top_kontrol": 80}, {"savunma": 65, "top_kapma": 72, "pozisyon": 69}),
    Futbolcu("Elyesa", {"hiz": 87, "sut": 79, "top_kontrol": 80}, {"pas": 80, "vizyon": 84, "top_kontrol": 80}, {"savunma": 74, "top_kapma": 76, "pozisyon": 74}),
    Futbolcu("Bekir", {"hiz": 76, "sut": 79, "top_kontrol": 74}, {"pas": 79, "vizyon": 75, "top_kontrol": 78}, {"savunma": 77, "top_kapma": 78, "pozisyon": 74}),
    Futbolcu("Burak Can", {"hiz": 74, "sut": 80, "top_kontrol": 78}, {"pas": 78, "vizyon": 80, "top_kontrol": 78}, {"savunma": 70, "top_kapma": 70, "pozisyon": 71}),
    Futbolcu("Serhan", {"hiz": 80, "sut": 76, "top_kontrol": 80}, {"pas": 75, "vizyon": 82, "top_kontrol": 80}, {"savunma": 70, "top_kapma": 72, "pozisyon": 74}),
    Futbolcu("Esad", {"hiz": 80, "sut": 70, "top_kontrol": 72}, {"pas": 72, "vizyon": 70, "top_kontrol": 71}, {"savunma": 71, "top_kapma": 73, "pozisyon": 76}),
    Futbolcu("Dutucu", {"hiz": 73, "sut": 76, "top_kontrol": 83}, {"pas": 85, "vizyon": 85, "top_kontrol": 81}, {"savunma": 69, "top_kapma": 68, "pozisyon": 73})
]

futbolcular.sort(key=lambda x: x.toplam_puan(), reverse=True)

takim1 = []
takim2 = []

toplam_puan_takim1 = 0
toplam_puan_takim2 = 0

for i, futbolcu in enumerate(futbolcular):
    if toplam_puan_takim1 <= toplam_puan_takim2:
        takim1.append(futbolcu)
        toplam_puan_takim1 += futbolcu.toplam_puan()
    else:
        takim2.append(futbolcu)
        toplam_puan_takim2 += futbolcu.toplam_puan()

print("Takım 1:")
for futbolcu in takim1:
    showBilgi(futbolcu)

print("Takım 2:")
for futbolcu in takim2:
    showBilgi(futbolcu)

print(f"\nTakım 1 Toplam Puan: {toplam_puan_takim1}")
print(f"Takım 2 Toplam Puan: {toplam_puan_takim2}")
print("--------------------- Takım 1 ---------------------")
for futbolcu in takim1:
    print(futbolcu.ad)
print("--------------------- Takım 2 ---------------------")
for futbolcu in takim2:
    print(futbolcu.ad)
