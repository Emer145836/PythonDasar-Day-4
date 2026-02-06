import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa")

nama_depan = tk.StringVar()
nama_belakang = tk.StringVar()

def tombol_click():
    pesan=f"Hello {nama_depan.get()} {nama_belakang.get()}, Have a nice day"
    showinfo(title="Hi", message=pesan)

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

nama_depan_entry = ttk.Entry(input_frame, textvariable=nama_depan)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx= 10, fill="x", expand=True)

nama_belakang_entry = ttk.Entry(input_frame, textvariable=nama_belakang)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

tombol = ttk.Button(input_frame,text="Sapa!", command=tombol_click)
tombol.pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()