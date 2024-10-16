import random

def tekMi(sayi):
    if sayi % 2 == 0:
        print("Girdiğiniz değer tek sayı değil!")
        return False
    else:
        return True

bot = 0
player = 0
hareketler = ['tas', 'kagit', 'makas']

tur = int(input("Kaç tur oynanacağını giriniz: "))

if tekMi(tur): 
    while tur != 0:
        botSecim = random.choice(hareketler)
        print(f'Botun seçimi: {botSecim} | Kalan tur: {tur}')
        
        while True:
            playerSecim = input("Hareketinizi seçiniz (tas, kagit, makas): ").lower()
            if playerSecim in hareketler:
                break
            print("Geçersiz hareket, tekrar deneyin!")
        
        if botSecim == playerSecim:
            print("Berabere!")
        elif (botSecim == 'tas' and playerSecim == 'kagit') or \
             (botSecim == 'kagit' and playerSecim == 'makas') or \
             (botSecim == 'makas' and playerSecim == 'tas'):
            player += 1
            print("Kazandın!")
        else:
            bot += 1
            print("Bot Kazandı!")
        
        tur -= 1

    print(f"\nSonuç: Oyuncu {player} - {bot} Bot")
else:
    print("Oyun bitirildi.")
