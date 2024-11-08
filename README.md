Számológép - Python Tkinter Alapú
Ez a projekt egy egyszerű, grafikus számológép, amelyet Python és a Tkinter könyvtár segítségével készítettünk. A számológép támogatja az alapvető aritmetikai műveleteket (összeadás, kivonás, szorzás, osztás) és egy "Törlés" funkciót, hogy gyorsan lehessen törölni a bevitt adatokat.

Fő funkciók
Alapvető műveletek: Összeadás, kivonás, szorzás, osztás.
Törlés gomb: Törli az aktuális számítást.
Esztétikus elrendezés és design: Világos színpaletta a gombok és a háttér számára, kiemelve a műveleti és "Törlés" gombokat.
Eredménykijelző: Nagy, jól olvasható kijelző a számítási eredmények számára.
Használat
Futtassa a kódot Python 3 környezetben.
A program megnyit egy számológép ablakot, amelyben a gombok segítségével elvégezhetők a kívánt műveletek.
A számítás végeredményéhez nyomja meg az = gombot.
A törléshez használja a Törlés gombot, amely alaphelyzetbe állítja a számológépet.
Rendszerkövetelmények
Python 3.x: A kód Python 3.6 vagy újabb verzióval működik.
Tkinter: A Tkinter könyvtár, amely alapértelmezetten a Python telepítés részét képezi.
Telepítés és futtatás
Győződjön meg róla, hogy Python 3 telepítve van a rendszeren.
Mentse a kódot egy .py fájlba (például szamologep.py).
Nyisson meg egy terminál ablakot, és futtassa az alábbi parancsot:
python szamologep.py
Kód áttekintése
Eredménykijelző: Az eredmények megjelenítésére szolgáló szöveg tk.Label widget segítségével lett létrehozva.
Gombok: A gombok színesek és szegéllyel rendelkeznek. A Törlés gomb külön sorban, teljes szélességben helyezkedik el, míg az egyenlőség (=) gomb két cellát foglal el, hogy kiemelkedjen.
Színkódok:
Számgombok: Világosszürke (#D3D3D3).
Műveleti gombok: Világoszöld (#8FCB9B).
Törlés gomb: Pirosas szín (#FF6666).
