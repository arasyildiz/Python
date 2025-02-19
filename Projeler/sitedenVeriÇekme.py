import requests
import tkinter as tk
from tkinter import messagebox

# kodu çalıştırabilmek için openweathermap sitesine kayıt olmanız lazım
# kayıt olduktan sonra size mail gelecek maildeki api keyinizi alt kısma girin, key 2 3 dakika içinde aktif oluyor.
# günlük 1k sınırı var. Kütüphaneleri indirmeyi unutmayın
API_KEY = "buraya api keyinizi giriniz"

def hava_durumu_getir():
    sehir = sehir_giris.get()
    ulke = ulke_giris.get()
    
    if not sehir or not ulke:
        messagebox.showerror("Hata", "Lütfen şehir ve ülke kodunu girin!")
        return
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir},{ulke}&appid={API_KEY}&units=metric"
    cevap = requests.get(url).json() # burada bilerek json olarak çektim ki eğer yanlış bir değer girilirse kontrol edip hata mesajı verebileyim.
    
    if cevap.get("cod") != 200:
        messagebox.showerror("Hata", "Şehir bulunamadı!")
        return
    
    sicaklik = cevap["main"]["temp"]
    basinc = cevap["main"]["pressure"]
    nem = cevap["main"]["humidity"]
    sonuc_etiket.config(text=f"Sıcaklık: {sicaklik}°C\nBasınç: {basinc} hPa\nNem: %{nem}")

root = tk.Tk()
root.title("Hava Durumu")
root.geometry("300x200")

tk.Label(root, text="Şehir:").pack()
sehir_giris = tk.Entry(root)
sehir_giris.pack()

tk.Label(root, text="Ülke Kodu:").pack()
ulke_giris = tk.Entry(root)
ulke_giris.pack()

tk.Button(root, text="Hava Durumunu Getir", command=hava_durumu_getir).pack(pady=10)

sonuc_etiket = tk.Label(root, text="")
sonuc_etiket.pack()

root.mainloop()
