import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import json
from pathlib import Path


class Futbolcu:
    def __init__(self, ad, forvet_ozellikler, ortasaha_ozellikler, defans_ozellikler):
        self.ad = ad
        self.forvet = forvet_ozellikler
        self.ortasaha = ortasaha_ozellikler
        self.defans = defans_ozellikler

    def toplam_puan(self):
        toplam = (sum(self.forvet.values()) + sum(self.ortasaha.values()) + sum(self.defans.values())) / 9
        return toplam


# Veri dosyası
DATA_FILE = Path("futbolcular.json")


def load_players():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return [Futbolcu(**player) for player in data]
    return []


def save_players():
    with open(DATA_FILE, "w") as file:
        json.dump(
            [
                {
                    "ad": p.ad,
                    "forvet_ozellikler": p.forvet,
                    "ortasaha_ozellikler": p.ortasaha,
                    "defans_ozellikler": p.defans,
                }
                for p in futbolcular
            ],
            file,
            indent=4,
        )


def display_team(team, tree):
    tree.delete(*tree.get_children())
    for player in team:
        tree.insert("", "end", values=(player.ad, f"{player.toplam_puan():.2f}"))


def add_player():
    try:
        ad = add_name_var.get()
        forvet = {"hiz": int(add_forvet_hiz.get()), "sut": int(add_forvet_sut.get()), "top_kontrol": int(add_forvet_kontrol.get())}
        ortasaha = {"pas": int(add_orta_pas.get()), "vizyon": int(add_orta_vizyon.get()), "top_kontrol": int(add_orta_kontrol.get())}
        defans = {"savunma": int(add_def_savunma.get()), "top_kapma": int(add_def_kapma.get()), "pozisyon": int(add_def_pozisyon.get())}

        yeni_futbolcu = Futbolcu(ad, forvet, ortasaha, defans)
        futbolcular.append(yeni_futbolcu)
        futbolcular.sort(key=lambda x: x.toplam_puan(), reverse=True)

        update_teams()
        save_players()
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


def delete_player():
    selected_player = player_selection_var.get()
    if selected_player:
        futbolcular[:] = [futbolcu for futbolcu in futbolcular if futbolcu.ad != selected_player]
        futbolcular.sort(key=lambda x: x.toplam_puan(), reverse=True)

        update_teams()
        save_players()
    else:
        print("Lütfen bir oyuncu seçin.")


def update_teams():
    takim1.clear()
    takim2.clear()
    toplam_puan_takim1, toplam_puan_takim2 = 0, 0

    for futbolcu in futbolcular:
        if toplam_puan_takim1 <= toplam_puan_takim2:
            takim1.append(futbolcu)
            toplam_puan_takim1 += futbolcu.toplam_puan()
        else:
            takim2.append(futbolcu)
            toplam_puan_takim2 += futbolcu.toplam_puan()

    display_team(takim1, team1_tree)
    display_team(takim2, team2_tree)

    # Oyuncuları dropdown'dan güncelle
    player_selection_menu["values"] = [futbolcu.ad for futbolcu in futbolcular]
    if player_selection_var.get() not in player_selection_menu["values"]:
        player_selection_var.set("")  # Seçili oyuncu silindiyse seçim sıfırlanır.


# Oyuncu Listesi
futbolcular = load_players()

takim1, takim2 = [], []

# Kullanıcı Arayüzü
root = tk.Tk()
root.title("Futbolcu Takım Yönetimi")

# Takım 1
team1_label = tk.Label(root, text="Takım 1")
team1_label.grid(row=0, column=0, padx=10, pady=5)

team1_tree = ttk.Treeview(root, columns=("Ad", "Puan"), show="headings", height=10)
team1_tree.heading("Ad", text="Ad")
team1_tree.heading("Puan", text="Puan")
team1_tree.grid(row=1, column=0, padx=10, pady=5)

# Takım 2
team2_label = tk.Label(root, text="Takım 2")
team2_label.grid(row=0, column=1, padx=10, pady=5)

team2_tree = ttk.Treeview(root, columns=("Ad", "Puan"), show="headings", height=10)
team2_tree.heading("Ad", text="Ad")
team2_tree.heading("Puan", text="Puan")
team2_tree.grid(row=1, column=1, padx=10, pady=5)

# Oyuncu Ekleme Alanı
add_frame = tk.LabelFrame(root, text="Oyuncu Ekle")
add_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

add_name_var = tk.StringVar()
tk.Label(add_frame, text="Ad").grid(row=0, column=0)
tk.Entry(add_frame, textvariable=add_name_var).grid(row=0, column=1)

add_forvet_hiz = tk.StringVar()
add_forvet_sut = tk.StringVar()
add_forvet_kontrol = tk.StringVar()
tk.Label(add_frame, text="Forvet Hız/Şut/Kontrol").grid(row=1, column=0)
tk.Entry(add_frame, textvariable=add_forvet_hiz).grid(row=1, column=1)
tk.Entry(add_frame, textvariable=add_forvet_sut).grid(row=1, column=2)
tk.Entry(add_frame, textvariable=add_forvet_kontrol).grid(row=1, column=3)

add_orta_pas = tk.StringVar()
add_orta_vizyon = tk.StringVar()
add_orta_kontrol = tk.StringVar()
tk.Label(add_frame, text="Orta Saha Pas/Vizyon/Kontrol").grid(row=2, column=0)
tk.Entry(add_frame, textvariable=add_orta_pas).grid(row=2, column=1)
tk.Entry(add_frame, textvariable=add_orta_vizyon).grid(row=2, column=2)
tk.Entry(add_frame, textvariable=add_orta_kontrol).grid(row=2, column=3)

add_def_savunma = tk.StringVar()
add_def_kapma = tk.StringVar()
add_def_pozisyon = tk.StringVar()
tk.Label(add_frame, text="Defans Savunma/Kapma/Pozisyon").grid(row=3, column=0)
tk.Entry(add_frame, textvariable=add_def_savunma).grid(row=3, column=1)
tk.Entry(add_frame, textvariable=add_def_kapma).grid(row=3, column=2)
tk.Entry(add_frame, textvariable=add_def_pozisyon).grid(row=3, column=3)

tk.Button(add_frame, text="Oyuncu Ekle", command=add_player).grid(row=4, column=0, columnspan=4)

# Oyuncu Seçimi ve Silme Alanı
delete_frame = tk.LabelFrame(root, text="Oyuncu Sil")
delete_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

player_selection_var = tk.StringVar()
player_selection_menu = ttk.Combobox(delete_frame, textvariable=player_selection_var)
player_selection_menu.grid(row=0, column=0)

tk.Button(delete_frame, text="Oyuncu Sil", command=delete_player).grid(row=0, column=1)

update_teams()

# Başlat
root.mainloop()
