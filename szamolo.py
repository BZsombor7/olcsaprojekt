import tkinter as tk

# Számológép alkalmazás osztálya
class Szamologep:
    def __init__(self, ablak):
        self.ablak = ablak
        self.ablak.title("Számológép")
        self.ablak.geometry("400x600")
        
        # Eredmény kijelző mező létrehozása
        self.eredmeny_valtozo = tk.StringVar()
        self.eredmeny_cimke = tk.Label(ablak, textvariable=self.eredmeny_valtozo, font=("Arial", 24), anchor="e", bg="white", fg="black")
        self.eredmeny_cimke.grid(row=0, column=0, columnspan=4, sticky="we", ipadx=10, ipady=20)
        
        # Kezdeti értékek
        self.jelenlegi_bemenet = ""
        
        # Gombok létrehozása
        gombok = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('Törlés', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (szoveg, sor, oszlop) in gombok:
            self.gomb_letrehozas(szoveg, sor, oszlop)
    
    # Gomb létrehozása függvény
    def gomb_letrehozas(self, szoveg, sor, oszlop):
        gomb = tk.Button(self.ablak, text=szoveg, font=("Arial", 18), command=lambda: self.gomb_megnyomas(szoveg))
        gomb.grid(row=sor, column=oszlop, sticky="nsew", ipadx=20, ipady=20)
        self.ablak.grid_rowconfigure(sor, weight=1)
        self.ablak.grid_columnconfigure(oszlop, weight=1)
    
    # Gomb megnyomás esemény kezelője
    def gomb_megnyomas(self, karakter):
        if karakter.isdigit() or karakter in "+-*/":
            self.jelenlegi_bemenet += karakter
            self.eredmeny_valtozo.set(self.jelenlegi_bemenet)
        elif karakter == "Törlés":
            self.jelenlegi_bemenet = ""
            self.eredmeny_valtozo.set("0")
        elif karakter == "=":
            try:
                eredmeny = eval(self.jelenlegi_bemenet)
                self.eredmeny_valtozo.set(eredmeny)
                self.jelenlegi_bemenet = str(eredmeny)
            except Exception:
                self.eredmeny_valtozo.set("Hiba")
                self.jelenlegi_bemenet = ""

# Tkinter alkalmazás inicializálása
ablak = tk.Tk()
alkalmazas = Szamologep(ablak)
ablak.mainloop()
