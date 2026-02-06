import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Hitung Total")
window.geometry("250x200")
window.resizable(False, False)

harga = tk.StringVar()
kuantitas = tk.StringVar()
total = tk.StringVar(value="Rp. 0.00")

def hitung_total():
    try:
        h = float(harga.get())
        k = float(kuantitas.get())
        hasil = h * k
        total.set(f"Rp. {hasil:,.2f}")
    except ValueError:
        total.set("Rp. 0.00")

frame = ttk.Frame(window, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Harga:").pack(anchor="w")
ttk.Entry(frame, textvariable=harga).pack(fill="x")

ttk.Label(frame, text="Kuantitas:").pack(anchor="w", pady=(10, 0))
ttk.Entry(frame, textvariable=kuantitas).pack(fill="x")

ttk.Button(frame, text="Hitung Total", command=hitung_total).pack(pady=10)

ttk.Label(frame, text="Total:").pack()
ttk.Label(frame, textvariable=total).pack()

window.mainloop()