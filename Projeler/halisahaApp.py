import tkinter as tk
from tkinter import ttk
import json
from pathlib import Path

class Futbolcu:
    def __init__(self, ad, hiz, sut, pas, dripling, savunma, mevki):
        self.ad = ad
        self.hiz = hiz
        self.sut = sut
        self.pas = pas
        self.dripling = dripling
        self.savunma = savunma
        self.mevki = mevki

    def reyting(self):
        return int((self.hiz + self.sut + self.pas + self.dripling + self.savunma) / 5)

    def to_dict(self):
        return {
            "ad": self.ad,
            "hiz": self.hiz,
            "sut": self.sut,
            "pas": self.pas,
            "dripling": self.dripling,
            "savunma": self.savunma,
            "mevki": self.mevki
        }

    @staticmethod
    def from_dict(data):
        return Futbolcu(
            data['ad'],
            data['hiz'],
            data['sut'],
            data['pas'],
            data['dripling'],
            data['savunma'],
            data['mevki']
        )

# Veriyi yüklemek için fonksiyon
def load_futbolcular():
    try:
        # Dosya yolunu kontrol etme
        file_path = Path("futbolcular.json")
        if not file_path.exists():
            print("Dosya bulunamadı, yeni dosya oluşturulacak.")
            return []  # Dosya yoksa boş liste döndür
        
        with open(file_path, "r") as file:
            data = json.load(file)
            # JSON verisini yüklerken her oyuncu için Futbolcu nesnesi oluşturuyoruz
            return [Futbolcu.from_dict(player) for player in data]
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return []  # Dosya yoksa boş liste döndür
    except json.JSONDecodeError:
        print("JSON format hatası oluştu.")
        return []  # JSON format hatası varsa boş liste döndür
    except Exception as e:
        print(f"Bilinmeyen hata: {e}")
        return []  # Diğer hata durumları


# Oyuncu silme
def delete_player():
    # Seçilen satırı al
    selected_item = tree.selection()  # Treeview'deki seçilen öğeyi alıyoruz
    if selected_item:
        # Seçilen oyuncunun adını al
        selected_player_name = tree.item(selected_item[0], "values")[0]

        # futbolcular listesinden bu oyuncuyu sil
        global futbolcular  # futbolcular listesine global erişim sağlıyoruz
        futbolcular = [futbolcu for futbolcu in futbolcular if futbolcu.ad != selected_player_name]

        # JSON dosyasını güncelle
        save_futbolcular()

        # Treeview'i tekrar güncelle
        display_futbolcular()

        print(f"{selected_player_name} başarıyla silindi.")
    else:
        print("Lütfen bir oyuncu seçin.")


# Veriyi kaydetmek için fonksiyon
def save_futbolcular():
    try:
        with open("futbolcular.json", "w") as file:
            json.dump([futbolcu.to_dict() for futbolcu in futbolcular], file, indent=4)
    except Exception as e:
        print(f"Veri kaydedilirken hata oluştu: {e}")


# Futbolcuları gösterme
def display_futbolcular():
    tree.delete(*tree.get_children())
    for futbolcu in futbolcular:
        tree.insert("", "end", values=(futbolcu.ad, futbolcu.reyting(), futbolcu.mevki))

# Oyuncu ekleme
def add_player():
    ad = add_name_var.get()
    hiz = int(add_hiz_var.get())
    sut = int(add_sut_var.get())
    pas = int(add_pas_var.get())
    dripling = int(add_dripling_var.get())
    savunma = int(add_savunma_var.get())
    mevki = add_mevki_var.get()  # Seçilen mevkiyi alıyoruz

    yeni_futbolcu = Futbolcu(ad, hiz, sut, pas, dripling, savunma, mevki)
    futbolcular.append(yeni_futbolcu)
    save_futbolcular()
    display_futbolcular()

# Oyuncu silme
def delete_player():
    selected_item = tree.selection()
    if selected_item:
        selected_player = tree.item(selected_item[0], "values")[0]
        futbolcular[:] = [futbolcu for futbolcu in futbolcular if futbolcu.ad != selected_player]
        save_futbolcular()
        display_futbolcular()

# Oyuncu düzenleme
def edit_player():
    selected_item = tree.selection()
    if selected_item:
        selected_player = tree.item(selected_item[0], "values")[0]
        for futbolcu in futbolcular:
            if futbolcu.ad == selected_player:
                try:
                    futbolcu.hiz = int(edit_hiz_var.get()) if edit_hiz_var.get() else futbolcu.hiz
                    futbolcu.sut = int(edit_sut_var.get()) if edit_sut_var.get() else futbolcu.sut
                    futbolcu.pas = int(edit_pas_var.get()) if edit_pas_var.get() else futbolcu.pas
                    futbolcu.dripling = int(edit_dripling_var.get()) if edit_dripling_var.get() else futbolcu.dripling
                    futbolcu.savunma = int(edit_savunma_var.get()) if edit_savunma_var.get() else futbolcu.savunma
                    futbolcu.mevki = edit_mevki_var.get() if edit_mevki_var.get() else futbolcu.mevki  # Mevkiyi düzenliyoruz

                    save_futbolcular()
                    display_futbolcular()
                except ValueError:
                    print("Lütfen geçerli bir sayısal değer girin.")
                break

# Takım oluşturma (mevki ve reyting göz önüne alınarak)

# Takım oluşturma ve görüntü düzenlemesi (Aşağıya doğru sıralama)
# Takım oluşturma ve görüntü düzenlemesi (Yan yana sıralama, arka plan kaldırma)
def create_teams():
    # Mevkilere göre futbolcuları grupla
    mevkilere_gore = {"Santrafor": [], "Ortasaha": [], "Defans": []}
    for futbolcu in futbolcular:
        mevkilere_gore[futbolcu.mevki].append(futbolcu)

    team1, team2 = [], []

    # Her mevkiden oyuncuları reytinglerine göre sırala
    for mevki in mevkilere_gore:
        mevki_futbolcular = sorted(mevkilere_gore[mevki], key=lambda x: x.reyting(), reverse=True)

        # Reytinglere göre oyuncuları sırayla takım 1 ve takım 2'ye yerleştir
        for i in range(len(mevki_futbolcular)):
            if i % 2 == 0:
                team1.append(mevki_futbolcular[i])
            else:
                team2.append(mevki_futbolcular[i])

    # Takım 1 ve Takım 2'nin eşit sayıda olduğundan emin olalım
    while len(team1) != len(team2):
        if len(team1) > len(team2):
            team2.append(team1.pop())  # Takım 1'den oyuncu alıp Takım 2'ye ekle
        else:
            team1.append(team2.pop())  # Takım 2'den oyuncu alıp Takım 1'e ekle

    # Takımların oyuncu isimlerini güncelle
    team1_names = [player.ad for player in team1]
    team2_names = [player.ad for player in team2]

    # Takım 1 için etiketler (yan yana)
    team1_frame = tk.Frame(team_buttons_frame)
    team1_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    max_length = max(len(team1_names), len(team2_names))
    font_size = 14  # Başlangıç yazı tipi boyutu

    # Eğer oyuncu sayısı çok fazla ise, yazı tipini küçült
    if max_length > 20:
        font_size = 10  # Çok fazla oyuncu varsa yazı tipi daha küçük
    if max_length > 30:
        font_size = 8  # Çok daha fazla oyuncu varsa daha da küçült

    # Takım 1 oyuncuları için etiketler
    for i, player in enumerate(team1_names):
        tk.Label(team1_frame, text=player, font=("Arial", font_size), fg="black", pady=5, padx=10, relief="solid", bd=1).grid(row=i, column=0, sticky="w")

    # Takım 2 için etiketler (yan yana)
    team2_frame = tk.Frame(team_buttons_frame)
    team2_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Takım 2 oyuncuları için etiketler
    for i, player in enumerate(team2_names):
        tk.Label(team2_frame, text=player, font=("Arial", font_size), fg="black", pady=5, padx=10, relief="solid", bd=1).grid(row=i, column=0, sticky="w")


# Ana pencere
root = tk.Tk()
root.title("Halısaha Takım Yönetimi")
root.geometry("1200x800")  

futbolcular = load_futbolcular()


tree = ttk.Treeview(root, columns=("Ad", "Reyting", "Mevki"), show="headings", height=15)
tree.heading("Ad", text="Ad", anchor="w")
tree.heading("Reyting", text="Reyting", anchor="w")
tree.heading("Mevki", text="Mevki", anchor="w")
tree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


form_frame = tk.Frame(root)
form_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="#4CAF50", foreground="white", padding=10)
style.map("TButton", background=[("active", "#45a049")])
style.configure("TLabel", font=("Arial", 12), background="#f4f4f4")

# Oyuncu ekleme kısmı
add_frame = tk.LabelFrame(form_frame, text="Oyuncu Ekle", font="Arial 14 bold", bg="#e0f7fa")
add_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

add_name_var = tk.StringVar()
add_hiz_var = tk.StringVar()
add_sut_var = tk.StringVar()
add_pas_var = tk.StringVar()
add_dripling_var = tk.StringVar()
add_savunma_var = tk.StringVar()
add_mevki_var = tk.StringVar()

tk.Label(add_frame, text="Ad:", font="Arial 12", bg="#e0f7fa").grid(row=0, column=0, pady=5, sticky="e")
tk.Entry(add_frame, textvariable=add_name_var, font="Arial 12").grid(row=0, column=1, pady=5)

tk.Label(add_frame, text="Hız:", font="Arial 12", bg="#e0f7fa").grid(row=1, column=0, pady=5, sticky="e")
tk.Entry(add_frame, textvariable=add_hiz_var, font="Arial 12").grid(row=1, column=1, pady=5)

tk.Label(add_frame, text="Şut:", font="Arial 12", bg="#e0f7fa").grid(row=2, column=0, pady=5, sticky="e")
tk.Entry(add_frame, textvariable=add_sut_var, font="Arial 12").grid(row=2, column=1, pady=5)

tk.Label(add_frame, text="Pas:", font="Arial 12", bg="#e0f7fa").grid(row=3, column=0, pady=5, sticky="e")
tk.Entry(add_frame, textvariable=add_pas_var, font="Arial 12").grid(row=3, column=1, pady=5)

tk.Label(add_frame, text="Dripling:", font="Arial 12", bg="#e0f7fa").grid(row=4, column=0, pady=5, sticky="e")
tk.Entry(add_frame, textvariable=add_dripling_var, font="Arial 12").grid(row=4, column=1, pady=5)

tk.Label(add_frame, text="Savunma:", font="Arial 12", bg="#e0f7fa").grid(row=5, column=0, pady=5, sticky="e")
tk.Entry(add_frame, textvariable=add_savunma_var, font="Arial 12").grid(row=5, column=1, pady=5)

tk.Label(add_frame, text="Mevki:", font="Arial 12", bg="#e0f7fa").grid(row=6, column=0, pady=5, sticky="e")
mevki_choices = ["Santrafor", "Ortasaha", "Defans"]
add_mevki_menu = ttk.Combobox(add_frame, textvariable=add_mevki_var, values=mevki_choices, state="readonly", font="Arial 12")
add_mevki_menu.grid(row=6, column=1, pady=5)

tk.Button(add_frame, text="Ekle", command=add_player).grid(row=7, column=0, columnspan=2, pady=10)

edit_frame = tk.LabelFrame(form_frame, text="Oyuncu Düzenle", font="Arial 14 bold", bg="#e0f7fa")
edit_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

edit_hiz_var = tk.StringVar()
edit_sut_var = tk.StringVar()
edit_pas_var = tk.StringVar()
edit_dripling_var = tk.StringVar()
edit_savunma_var = tk.StringVar()
edit_mevki_var = tk.StringVar()

tk.Label(edit_frame, text="Yeni Hız:", font="Arial 12", bg="#e0f7fa").grid(row=0, column=0, pady=5, sticky="e")
tk.Entry(edit_frame, textvariable=edit_hiz_var, font="Arial 12").grid(row=0, column=1, pady=5)

tk.Label(edit_frame, text="Yeni Şut:", font="Arial 12", bg="#e0f7fa").grid(row=1, column=0, pady=5, sticky="e")
tk.Entry(edit_frame, textvariable=edit_sut_var, font="Arial 12").grid(row=1, column=1, pady=5)

tk.Label(edit_frame, text="Yeni Pas:", font="Arial 12", bg="#e0f7fa").grid(row=2, column=0, pady=5, sticky="e")
tk.Entry(edit_frame, textvariable=edit_pas_var, font="Arial 12").grid(row=2, column=1, pady=5)

tk.Label(edit_frame, text="Yeni Dripling:", font="Arial 12", bg="#e0f7fa").grid(row=3, column=0, pady=5, sticky="e")
tk.Entry(edit_frame, textvariable=edit_dripling_var, font="Arial 12").grid(row=3, column=1, pady=5)

tk.Label(edit_frame, text="Yeni Savunma:", font="Arial 12", bg="#e0f7fa").grid(row=4, column=0, pady=5, sticky="e")
tk.Entry(edit_frame, textvariable=edit_savunma_var, font="Arial 12").grid(row=4, column=1, pady=5)

tk.Label(edit_frame, text="Yeni Mevki:", font="Arial 12", bg="#e0f7fa").grid(row=5, column=0, pady=5, sticky="e")
edit_mevki_menu = ttk.Combobox(edit_frame, textvariable=edit_mevki_var, values=mevki_choices, state="readonly", font="Arial 12")
edit_mevki_menu.grid(row=5, column=1, pady=5)

tk.Button(edit_frame, text="Düzenle", command=edit_player).grid(row=6, column=0, columnspan=2, pady=10)

delete_button = tk.Button(root, text="Oyuncu Sil", font="Arial 12", command=delete_player)
delete_button.grid(row=0, column=2, padx=10, pady=10)

team_buttons_frame = tk.Frame(root)
team_buttons_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

create_team_button = tk.Button(team_buttons_frame, text="Takım Oluştur", font="Arial 12", command=create_teams)
create_team_button.grid(row=0, column=0, padx=10, pady=10)

team1_label = tk.Label(team_buttons_frame, text="Takım 1: ", font="Arial 12")
team1_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

team2_label = tk.Label(team_buttons_frame, text="Takım 2: ", font="Arial 12")
team2_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

root.mainloop()
