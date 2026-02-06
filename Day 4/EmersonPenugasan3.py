import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("MainWindow")
window.geometry("600x650")
window.resizable(False, False)

header = tk.Label(
    window,
    text="DATA SISWA BARU",
    bg="#9ee7ea",
    fg="black",
    font=("Arial", 16, "bold"),
    pady=15
)
header.pack(fill="x")

form = ttk.Frame(window, padding=15)
form.pack(fill="both", expand=True)

def buat_input(label_text):
    ttk.Label(form, text=label_text).pack(anchor="w")
    entry = ttk.Entry(form)
    entry.pack(fill="x", pady=5)
    return entry

nama_lengkap = buat_input("Nama Lengkap")
tanggal_lahir = buat_input("Tanggal Lahir")
asal_sekolah = buat_input("Asal Sekolah")
nisn = buat_input("NISN")
nama_ayah = buat_input("Nama Ayah")
nama_ibu = buat_input("Nama Ibu")
no_hp = buat_input("Nomor Telepon / HP")

ttk.Label(form, text="Alamat").pack(anchor="w")
alamat = tk.Text(form, height=5)
alamat.pack(fill="x", pady=5)

def hapus():
    for widget in form.winfo_children():
        if isinstance(widget, ttk.Entry):
            widget.delete(0, tk.END)
    alamat.delete("1.0", tk.END)

def simpan():
    messagebox.showinfo("Simpan", "Data berhasil disimpan!")

btn_frame = ttk.Frame(window, padding=10)
btn_frame.pack(fill="x", side="bottom")

btn_hapus = tk.Button(
    btn_frame, text="Hapus", bg="#d97b5f", fg="white",
    width=12, command=hapus
)
btn_hapus.pack(side="right", padx=5)

btn_simpan = tk.Button(
    btn_frame, text="Simpan", bg="#d97b5f", fg="white",
    width=12, command=simpan
)
btn_simpan.pack(side="right", padx=5)

window.mainloop()