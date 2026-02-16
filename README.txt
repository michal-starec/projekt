=============================
   Správa herních turnajů
=============================

Popis aplikace:
----------------
Tato aplikace slouží ke správě herních turnajů. Umožňuje:
- Spravovat seznam her (Přidat, Upravit, Smazat)
- Spravovat hráče turnaje (Přidat, Upravit, Smazat)
- Zadávat výsledky hráčů v jednotlivých hrách (Přidat, Upravit, Smazat)
- Přehledně zobrazovat data v tabulkách s možností výběru a editace
- Automaticky aktualizovat seznamy v ComboBoxech při změnách

Technologie:
-------------
- Python 3.x
- Tkinter pro GUI
- SQLite3 pro databázi
- Modularizovaná struktura: 
  * `gui.py` – hlavní GUI aplikace
  * `logika.py` – pomocné funkce, placeholdery
  * `databaze.py` – propojení s SQLite databází

Databázové tabulky:
-------------------
1. hry
   - id (INTEGER, PRIMARY KEY)
   - nazev (TEXT)
   - zanr (TEXT)
2. hraci
   - id (INTEGER, PRIMARY KEY)
   - jmeno (TEXT)
   - prezdivka (TEXT, UNIQUE)
3. vysledky
   - id (INTEGER, PRIMARY KEY)
   - hra_id (INTEGER, FOREIGN KEY -> hry.id)
   - hrac_id (INTEGER, FOREIGN KEY -> hraci.id)
   - skore (INTEGER)

Autoři a rozdělení práce:
--------------------------
1. [Michal Starec] –Databáze (vytvoření tabulek, CRUD funkce)
2. [Ivan Hlushko] – Logika aplikace (funkce, placeholdery, načítání dat)
3. [Daniel Vacek] – GUI (vytvoření oken, Treeview, tlačítek)
4. [Tomáš Jelínek] – Testování aplikace, kontrola funkcionality a opravování chyb


Instrukce k spuštění:
---------------------
1. Ujistěte se, že máte nainstalovaný Python 3.x.
2. Umístěte soubory `gui.py`, `logika.py` a `databaze.py` ve stejné složce.
3. Spusťte terminál/cmd ve složce s projektem.
4. Spusťte příkaz: `python gui.py`
5. Aplikace se otevře a bude připravena k použití.

Poznámky:
----------
- Při prvním spuštění se automaticky vytvoří databáze `turnaje.db`.
- Tlačítka Přidat, Upravit a Smazat jsou dostupná u každé záložky.
- Změny se ukládají okamžitě do databáze.

=======================================
