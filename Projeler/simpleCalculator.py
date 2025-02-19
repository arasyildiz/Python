def calculator():
    try:
        a = float(input("Birinci sayıyı girin: "))
        b = float(input("İkinci sayıyı girin: "))
        islem = input("İşlem (+, -, *, /): ")

        if islem == "+":
            print("Sonuç:", a + b)
        elif islem == "-":
            print("Sonuç:", a - b)
        elif islem == "*":
            print("Sonuç:", a * b)
        elif islem == "/":
            print("Sonuç:", a / b if b != 0 else "Hata: Sıfıra bölünemez")
        else:
            print("Geçersiz işlem!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

calculator()
