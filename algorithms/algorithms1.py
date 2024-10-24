# Kullanıcının istediği büyüklükte bir diziyi 0-100 arasında rastgele oluşturulmuş
# sayılarla doldurup bu sayıların standart sapmasını hesaplayınız
import math
import random
diziBoyut = int(input("Dizinin boyutunu giriniz : "))
sayilar = []
toplam = 0
sToplam = 0
for i in range(diziBoyut):
    rastSayi = random.randint(0,100)
    sayilar.append(rastSayi)
    toplam +=  rastSayi
ort = toplam / diziBoyut 
for i in range(diziBoyut):
    sToplam = ((ort - sayilar[i]) ** 2) + sToplam
    
sSapma = math.sqrt((sToplam / diziBoyut)) 
print(f'toplam : {toplam}, ortalama : {ort}, sSapma = {sSapma}, \nDizinin içeriği : {sayilar}')
