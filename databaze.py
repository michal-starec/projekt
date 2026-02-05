import sqlite3

# Připojení k DB
conn = sqlite3.connect("turnaje.db")
cursor = conn.cursor()

# Vytvoření tabulek
cursor.execute("""
CREATE TABLE IF NOT EXISTS hry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazev TEXT NOT NULL,
    zanr TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS hraci (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jmeno TEXT NOT NULL,
    prezdivka TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vysledky (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hra_id INTEGER NOT NULL,
    hrac_id INTEGER NOT NULL,
    skore INTEGER NOT NULL
)
""")
conn.commit()
