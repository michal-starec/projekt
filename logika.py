from databaze import conn, cursor

# ================= PLACEHOLDER =================
def placeholder(entry, text):
    entry.insert(0, text)
    entry.config(foreground="gray", background="white")

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, "end")
        entry.config(foreground="black")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, text)
            entry.config(foreground="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# ================= CRUD & načítání =================
def load_hry(tree):
    tree.delete(*tree.get_children())
    for r in cursor.execute("SELECT * FROM hry"):
        tree.insert("", "end", values=r)

def load_hraci(tree):
    tree.delete(*tree.get_children())
    for r in cursor.execute("SELECT * FROM hraci"):
        tree.insert("", "end", values=r)

def load_vys(tree):
    tree.delete(*tree.get_children())
    cursor.execute("""
        SELECT vysledky.id, hry.nazev, hraci.prezdivka, vysledky.skore
        FROM vysledky
        JOIN hry ON hry.id=vysledky.hra_id
        JOIN hraci ON hraci.id=vysledky.hrac_id
        ORDER BY vysledky.skore DESC
    """)
    for r in cursor.fetchall():
        tree.insert("", "end", values=r)

def load_combos(cb_hra, cb_hrac):
    cursor.execute("SELECT id,nazev FROM hry")
    cb_hra["values"] = [f"{i} - {n}" for i,n in cursor.fetchall()]
    cursor.execute("SELECT id,prezdivka FROM hraci")
    cb_hrac["values"] = [f"{i} - {p}" for i,p in cursor.fetchall()]
