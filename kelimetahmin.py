import random

kelimeler = ['uzum', 'armut']
kullanilanHarfler = []

bittiMi = False
hak = 10

secilenKelime = kelimeler[random.randint(0, (len(kelimeler) - 1))]
yildizliKelime = '*' * len(secilenKelime)
print(secilenKelime)  
secilenKelime = secilenKelime.lower()

def kelimeyiGuncelle(secilenKelime, yildizliKelime, gelenCevap):
    yeniKelime = ''
    for i in range(len(secilenKelime)):
        if secilenKelime[i] == gelenCevap:
            yeniKelime += gelenCevap
        else:
            yeniKelime += yildizliKelime[i]
    return yeniKelime

while not bittiMi:
    if hak > 0:
        print(f"\nKelime: {yildizliKelime}")
        gelenCevap = input("| Bir harf giriniz: ").lower()

        if len(gelenCevap) != 1 or not gelenCevap.isalpha():
            print("| Lütfen sadece bir harf giriniz |")
            continue

        if gelenCevap in kullanilanHarfler:
            print("| Bu harfi zaten kullandınız |")
        else:
            kullanilanHarfler.append(gelenCevap)

            if gelenCevap in secilenKelime:
                print("| Harf doğru |")
                yildizliKelime = kelimeyiGuncelle(secilenKelime, yildizliKelime, gelenCevap)

                if yildizliKelime == secilenKelime:
                    print(f"| Kelime doğru! Kelime: {secilenKelime} |")
                    bittiMi = True
            else:
                print("| Yanlış harf |")
                hak -= 1
                print(f"Kullanılan Harfler: {kullanilanHarfler}, Kalan hakkınız: {hak}")
    else:
        print(f"Hakkınız kalmadı! Kelime: {secilenKelime}")
        bittiMi = True
