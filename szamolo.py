import tkinter as tk

# lobális változó a számológép bemenetéhez
jelenlegi_bemenet = ""

def gomb_megnyomas(karakter):
    global jelenlegi_bemenet
    if karakter.isdigit() or karakter in "+-*/":
        jelenlegi_bemenet += karakter
        eredmeny_valtozo.set(jelenlegi_bemenet)
    elif karakter == "Törlés":
        jelenlegi_bemenet = ""
        eredmeny_valtozo.set("0")
    elif karakter == "=":
        try:
            eredmeny = eval(jelenlegi_bemenet)
            eredmeny_valtozo.set(eredmeny)
            jelenlegi_bemenet = str(eredmeny)
        except Exception:
            eredmeny_valtozo.set("Hiba")
            jelenlegi_bemenet = ""

#Fő ablak
ablak = tk.Tk()
ablak.title("Számológép")
ablak.geometry("400x600")
ablak.configure(bg="#F0F0F0")

#Szines
eredmeny_valtozo = tk.StringVar()
eredmeny_valtozo.set("0")
eredmeny_cimke = tk.Label(
    ablak, textvariable=eredmeny_valtozo, font=("Arial", 32), anchor="e",
    bg="#FFFFFF", fg="#333333", padx=10, pady=20, borderwidth=2, relief="solid"
)
eredmeny_cimke.grid(row=0, column=0, columnspan=4, sticky="we")

#Törlés gomb
torles_gomb = tk.Button(
    ablak, text="Törlés", font=("Arial", 18), bg="#FF6666", fg="black",
    command=lambda: gomb_megnyomas("Törlés"), activebackground="#A9A9A9",
    relief="solid", borderwidth=2, padx=2, pady=2
)
torles_gomb.grid(row=1, column=0, columnspan=4, sticky="nsew", ipadx=10, ipady=20)

#Számok és műveleti gombok matrixa
gombok = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('+', 5, 3)
]

#Gombok és helyük
for szoveg, sor, oszlop in gombok:
    szin = "#D3D3D3" if szoveg.isdigit() or szoveg == "0" else "#8FCB9B"
    gomb = tk.Button(
        ablak, text=szoveg, font=("Arial", 18), bg=szin, fg="black",
        command=lambda szoveg=szoveg: gomb_megnyomas(szoveg), 
        activebackground="#A9A9A9", relief="solid", borderwidth=2, padx=10, pady=10
    )
    gomb.grid(row=sor, column=oszlop, sticky="nsew", ipadx=10, ipady=20)
    ablak.grid_rowconfigure(sor, weight=1)
    ablak.grid_columnconfigure(oszlop, weight=1)

# = gomb nagyobb
egyenloseg_gomb = tk.Button(
    ablak, text="=", font=("Arial", 18), bg="#8FCB9B", fg="black",
    command=lambda: gomb_megnyomas("="), activebackground="#A9A9A9",
    relief="solid", borderwidth=2, padx=10, pady=10
)
egyenloseg_gomb.grid(row=5, column=1, columnspan=2, sticky="nsew", ipadx=10, ipady=20)

ablak.mainloop()
