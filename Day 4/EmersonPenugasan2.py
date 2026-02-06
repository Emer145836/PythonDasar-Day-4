import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import math

BIAYA_PER_JAM = 2000

class AplikasiParkir:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Parkir Kelompok 6")
        self.root.geometry("900x450")

        self.data_parkir = []

        self.buat_ui()

    def buat_ui(self):
        frame_input = tk.Frame(self.root)
        frame_input.pack(side=tk.LEFT, padx=20, pady=20)

        tk.Label(frame_input, text="Aplikasi Parkir Kelompok 6",
                 font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

        tk.Label(frame_input, text="Cari NoPol").grid(row=1, column=0, sticky="w")
        self.entry_cari = tk.Entry(frame_input)
        self.entry_cari.grid(row=1, column=1)
        tk.Button(frame_input, text="Cari", command=self.cari).grid(row=1, column=2)

        tk.Label(frame_input, text="No Plat Polisi").grid(row=2, column=0, sticky="w")
        self.entry_plat = tk.Entry(frame_input)
        self.entry_plat.grid(row=2, column=1, columnspan=2, sticky="we")

        tk.Label(frame_input, text="Waktu Masuk (HH:MM)").grid(row=3, column=0, sticky="w")
        self.entry_masuk = tk.Entry(frame_input)
        self.entry_masuk.grid(row=3, column=1, columnspan=2, sticky="we")

        tk.Label(frame_input, text="Waktu Keluar (HH:MM)").grid(row=4, column=0, sticky="w")
        self.entry_keluar = tk.Entry(frame_input)
        self.entry_keluar.grid(row=4, column=1, columnspan=2, sticky="we")

        tk.Label(frame_input, text="Biaya").grid(row=5, column=0, sticky="w")
        self.var_biaya = tk.StringVar(value="0")
        tk.Entry(frame_input, textvariable=self.var_biaya,
                 state="readonly").grid(row=5, column=1)

        tk.Button(frame_input, text="Button", command=self.tambah_data)\
            .grid(row=5, column=2, padx=5)

        tk.Label(self.root, text="Biaya Per Jam\nRp. 2.000",
                 font=("Arial", 18, "bold"), fg="red")\
            .pack(side=tk.TOP, pady=20)

        frame_list = tk.Frame(self.root)
        frame_list.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=20)

        tk.Label(frame_list, text="List Pelanggan Urut Terakhir Keluar",
                 fg="blue").grid(row=0, column=0)

        tk.Label(frame_list, text="List Pelanggan Banyak Bayar",
                 fg="blue").grid(row=0, column=1)

        kolom = ("plat", "masuk", "keluar", "biaya")

        self.tree_terakhir = ttk.Treeview(frame_list, columns=kolom, show="headings")
        self.tree_banyak = ttk.Treeview(frame_list, columns=kolom, show="headings")

        for tree in (self.tree_terakhir, self.tree_banyak):
            tree.heading("plat", text="No Plat Polisi")
            tree.heading("masuk", text="Masuk")
            tree.heading("keluar", text="Keluar")
            tree.heading("biaya", text="Biaya")
            tree.column("biaya", width=80)

        self.tree_terakhir.grid(row=1, column=0, padx=10)
        self.tree_banyak.grid(row=1, column=1, padx=10)

    def hitung_biaya(self, masuk, keluar):
        fmt = "%H:%M"
        t_masuk = datetime.strptime(masuk, fmt)
        t_keluar = datetime.strptime(keluar, fmt)
        durasi_jam = math.ceil((t_keluar - t_masuk).seconds / 3600)
        return durasi_jam * BIAYA_PER_JAM

    def tambah_data(self):
        plat = self.entry_plat.get()
        masuk = self.entry_masuk.get()
        keluar = self.entry_keluar.get()

        if not plat or not masuk or not keluar:
            messagebox.showwarning("Peringatan", "Data belum lengkap!")
            return

        try:
            biaya = self.hitung_biaya(masuk, keluar)
        except:
            messagebox.showerror("Error", "Format waktu salah!")
            return

        self.var_biaya.set(str(biaya))

        data = (plat, masuk, keluar, biaya)
        self.data_parkir.append(data)

        self.tree_terakhir.insert("", 0, values=data)

        self.tree_banyak.delete(*self.tree_banyak.get_children())
        for d in sorted(self.data_parkir, key=lambda x: x[3], reverse=True):
            self.tree_banyak.insert("", "end", values=d)

    def cari(self):
        plat_cari = self.entry_cari.get()
        for item in self.tree_terakhir.get_children():
            if self.tree_terakhir.item(item)["values"][0] == plat_cari:
                self.tree_terakhir.selection_set(item)
                self.tree_terakhir.focus(item)
                return
        messagebox.showinfo("Info", "Plat tidak ditemukan")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiParkir(root)
    root.mainloop()