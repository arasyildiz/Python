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
    print(f"Toplam Puan: {x.toplam_puan()}")

aras = Futbolcu(
    ad="Aras",
    forvet_ozellikler={"hiz": 80, "sut": 80, "top_kontrol": 77},
    ortasaha_ozellikler={"pas": 78, "vizyon": 82, "top_kontrol": 80},
    defans_ozellikler={"savunma": 73, "top_kapma": 75, "pozisyon": 74}
)

berat = Futbolcu(
    ad="Berat",
    forvet_ozellikler={"hiz": 82, "sut": 85, "top_kontrol": 80},
    ortasaha_ozellikler={"pas": 84, "vizyon": 85, "top_kontrol": 83},
    defans_ozellikler={"savunma": 72, "top_kapma": 73, "pozisyon": 74}
)

eren = Futbolcu(
    ad="Eren",
    forvet_ozellikler={"hiz": 85, "sut": 85, "top_kontrol": 80},
    ortasaha_ozellikler={"pas": 84, "vizyon": 83, "top_kontrol": 83},
    defans_ozellikler={"savunma": 75, "top_kapma": 74, "pozisyon": 75}
)

boran = Futbolcu(
    ad="Boran",
    forvet_ozellikler={"hiz": 77, "sut": 73, "top_kontrol": 77},
    ortasaha_ozellikler={"pas": 79, "vizyon": 80, "top_kontrol": 79},
    defans_ozellikler={"savunma": 70, "top_kapma": 72, "pozisyon": 74}
)

mustafa = Futbolcu(
    ad="Mustafa",
    forvet_ozellikler={"hiz": 71, "sut": 70, "top_kontrol": 69},
    ortasaha_ozellikler={"pas": 73, "vizyon": 77, "top_kontrol": 70},
    defans_ozellikler={"savunma": 77, "top_kapma": 71, "pozisyon": 70}
)

murat = Futbolcu(
    ad="Murat",
    forvet_ozellikler={"hiz": 81, "sut": 73, "top_kontrol": 68},
    ortasaha_ozellikler={"pas": 71, "vizyon": 76, "top_kontrol": 67},
    defans_ozellikler={"savunma": 79, "top_kapma": 79, "pozisyon": 80}
)

mami = Futbolcu(
    ad="Mami",
    forvet_ozellikler={"hiz": 83, "sut": 81, "top_kontrol": 74},
    ortasaha_ozellikler={"pas": 79, "vizyon": 83, "top_kontrol": 74},
    defans_ozellikler={"savunma": 73, "top_kapma": 72, "pozisyon": 74}
)

bilal = Futbolcu(
    ad="Bilal",
    forvet_ozellikler={"hiz": 80, "sut": 82, "top_kontrol": 80},
    ortasaha_ozellikler={"pas": 84, "vizyon": 82, "top_kontrol": 80},
    defans_ozellikler={"savunma": 65, "top_kapma": 72, "pozisyon": 69}
)

elyesa = Futbolcu(
    ad="Elyesa",
    forvet_ozellikler={"hiz": 87, "sut": 79, "top_kontrol": 80},
    ortasaha_ozellikler={"pas": 80, "vizyon": 84, "top_kontrol": 80},
    defans_ozellikler={"savunma": 74, "top_kapma": 76, "pozisyon": 74}
)

bekir = Futbolcu(
    ad="Bekir",
    forvet_ozellikler={"hiz": 76, "sut": 79, "top_kontrol": 74},
    ortasaha_ozellikler={"pas": 79, "vizyon": 75, "top_kontrol": 78},
    defans_ozellikler={"savunma": 77, "top_kapma": 78, "pozisyon": 74}
)

burakcan = Futbolcu(
    ad="Burak Can",
    forvet_ozellikler={"hiz": 74, "sut": 80, "top_kontrol": 78},
    ortasaha_ozellikler={"pas": 78, "vizyon": 80, "top_kontrol": 78},
    defans_ozellikler={"savunma": 70, "top_kapma": 70, "pozisyon": 71}
)

serhan = Futbolcu(
    ad="Serhan",
    forvet_ozellikler={"hiz": 80, "sut": 76, "top_kontrol": 80},
    ortasaha_ozellikler={"pas": 75, "vizyon": 82, "top_kontrol": 80},
    defans_ozellikler={"savunma": 70, "top_kapma": 72, "pozisyon": 74}
)

esad = Futbolcu(
    ad="Esad",
    forvet_ozellikler={"hiz": 85, "sut": 85, "top_kontrol": 80},
    ortasaha_ozellikler={"pas": 84, "vizyon": 82, "top_kontrol": 80},
    defans_ozellikler={"savunma": 70, "top_kapma": 72, "pozisyon": 74}
)

dutucu = Futbolcu(
    ad="Dutucu",
    forvet_ozellikler={"hiz": 85, "sut": 85, "top_kontrol": 80},
    ortasaha_ozellikler={"pas": 84, "vizyon": 82, "top_kontrol": 80},
    defans_ozellikler={"savunma": 70, "top_kapma": 72, "pozisyon": 74}
)
showBilgi(bilal)


