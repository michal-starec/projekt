import tkinter as tk
from tkinter import ttk
from logika import placeholder
from databaze import cursor, conn

# ================= GLOBAL VARIABLES =================
selected_hra_id = None
selected_hrac_id = None
selected_vys_id = None

# ================= ROOT WINDOW =================
root = tk.Tk()
root.title("Správa herních turnajů")
root.geometry("1000x650")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("default")
style.configure("TFrame", background="#1e1e1e")
style.configure("TLabel", background="#1e1e1e", foreground="white")
style.configure("Treeview", background="#2b2b2b", foreground="white", rowheight=28)
style.configure("Treeview.Heading", background="#3c3f41", foreground="white")
style.map("Treeview", background=[("selected", "#007acc")])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# ================== HRY ==================
frame_hry = ttk.Frame(notebook)
notebook.add(frame_hry, text="🎮 Hry")

tree_hry = ttk.Treeview(frame_hry, columns=("id","nazev","zanr"), show="headings")
for c,t in zip(("id","nazev","zanr"), ("ID","Název","Žánr")):
    tree_hry.heading(c, text=t)
    tree_hry.column(c, anchor="center")
tree_hry.pack(fill="both", expand=True, pady=10)

form_hry = ttk.Frame(frame_hry)
form_hry.pack()

ttk.Label(form_hry, text="Název hry:").grid(row=0,column=0)
e_hra_nazev = tk.Entry(form_hry, width=30, bg="white")
e_hra_nazev.grid(row=0,column=1,padx=5)
placeholder(e_hra_nazev,"např. Fortnite")

ttk.Label(form_hry, text="Žánr:").grid(row=0,column=2)
e_hra_zanr = tk.Entry(form_hry, width=30, bg="white")
e_hra_zanr.grid(row=0,column=3,padx=5)
placeholder(e_hra_zanr,"např. Battle Royale")

# ======= Funkce pro HRY =======
def load_hry():
    tree_hry.delete(*tree_hry.get_children())
    for r in cursor.execute("SELECT * FROM hry"):
        tree_hry.insert("", "end", values=r)

def select_hra(e):
    global selected_hra_id
    item = tree_hry.item(tree_hry.selection())
    if item["values"]:
        selected_hra_id = item["values"][0]
        e_hra_nazev.delete(0,"end")
        e_hra_zanr.delete(0,"end")
        e_hra_nazev.insert(0,item["values"][1])
        e_hra_zanr.insert(0,item["values"][2])
        e_hra_nazev.config(foreground="black")
        e_hra_zanr.config(foreground="black")

tree_hry.bind("<<TreeviewSelect>>", select_hra)

def add_hra():
    cursor.execute("INSERT INTO hry (nazev,zanr) VALUES (?,?)", (e_hra_nazev.get(), e_hra_zanr.get()))
    conn.commit()
    load_hry()
    load_combos()

def update_hra():
    cursor.execute("UPDATE hry SET nazev=?, zanr=? WHERE id=?", (e_hra_nazev.get(), e_hra_zanr.get(), selected_hra_id))
    conn.commit()
    load_hry()

def delete_hra():
    cursor.execute("DELETE FROM vysledky WHERE hra_id=?", (selected_hra_id,))
    cursor.execute("DELETE FROM hry WHERE id=?", (selected_hra_id,))
    conn.commit()
    load_hry()
    load_vys()
    load_combos()

btns_hry = ttk.Frame(frame_hry)
btns_hry.pack(pady=5)
ttk.Button(btns_hry,text="➕ Přidat",command=add_hra).grid(row=0,column=0,padx=5)
ttk.Button(btns_hry,text="✏️ Upravit",command=update_hra).grid(row=0,column=1,padx=5)
ttk.Button(btns_hry,text="🗑️ Smazat",command=delete_hra).grid(row=0,column=2,padx=5)

load_hry()

# ================== HRÁČI ==================
frame_hraci = ttk.Frame(notebook)
notebook.add(frame_hraci, text="👤 Hráči")

tree_hraci = ttk.Treeview(frame_hraci, columns=("id","jmeno","prezdivka"), show="headings")
for c,t in zip(("id","jmeno","prezdivka"), ("ID","Jméno","Přezdívka")):
    tree_hraci.heading(c, text=t)
    tree_hraci.column(c, anchor="center")
tree_hraci.pack(fill="both", expand=True, pady=10)

form_hraci = ttk.Frame(frame_hraci)
form_hraci.pack()

ttk.Label(form_hraci,text="Jméno:").grid(row=0,column=0)
e_jmeno = tk.Entry(form_hraci,width=30, bg="white")
e_jmeno.grid(row=0,column=1,padx=5)
placeholder(e_jmeno,"např. Jan Novák")

ttk.Label(form_hraci,text="Přezdívka:").grid(row=0,column=2)
e_prez = tk.Entry(form_hraci,width=30, bg="white")
e_prez.grid(row=0,column=3,padx=5)
placeholder(e_prez,"unikátní nick")

# ======= Funkce pro HRÁČI =======
def load_hraci():
    tree_hraci.delete(*tree_hraci.get_children())
    for r in cursor.execute("SELECT * FROM hraci"):
        tree_hraci.insert("", "end", values=r)

def select_hrac(e):
    global selected_hrac_id
    item = tree_hraci.item(tree_hraci.selection())
    if item["values"]:
        selected_hrac_id = item["values"][0]
        e_jmeno.delete(0,"end")
        e_prez.delete(0,"end")
        e_jmeno.insert(0,item["values"][1])
        e_prez.insert(0,item["values"][2])
        e_jmeno.config(foreground="black")
        e_prez.config(foreground="black")

tree_hraci.bind("<<TreeviewSelect>>", select_hrac)

def add_hrac():
    cursor.execute("INSERT INTO hraci (jmeno,prezdivka) VALUES (?,?)", (e_jmeno.get(), e_prez.get()))
    conn.commit()
    load_hraci()
    load_combos()

def update_hrac():
    cursor.execute("UPDATE hraci SET jmeno=?, prezdivka=? WHERE id=?", (e_jmeno.get(), e_prez.get(), selected_hrac_id))
    conn.commit()
    load_hraci()
    load_combos()

def delete_hrac():
    cursor.execute("DELETE FROM vysledky WHERE hrac_id=?", (selected_hrac_id,))
    cursor.execute("DELETE FROM hraci WHERE id=?", (selected_hrac_id,))
    conn.commit()
    load_hraci()
    load_vys()
    load_combos()

btns_hraci = ttk.Frame(frame_hraci)
btns_hraci.pack(pady=5)
ttk.Button(btns_hraci,text="➕ Přidat",command=add_hrac).grid(row=0,column=0,padx=5)
ttk.Button(btns_hraci,text="✏️ Upravit",command=update_hrac).grid(row=0,column=1,padx=5)
ttk.Button(btns_hraci,text="🗑️ Smazat",command=delete_hrac).grid(row=0,column=2,padx=5)

load_hraci()

# ================== VÝSLEDKY ==================
frame_vys = ttk.Frame(notebook)
notebook.add(frame_vys, text="🏆 Výsledky")

form_vys = ttk.Frame(frame_vys)
form_vys.pack(pady=5)

ttk.Label(form_vys,text="Hra:").grid(row=0,column=0,padx=5)
cb_hra = ttk.Combobox(form_vys,width=25)
cb_hra.grid(row=0,column=1,padx=5)

ttk.Label(form_vys,text="Hráč:").grid(row=0,column=2,padx=5)
cb_hrac = ttk.Combobox(form_vys,width=25)
cb_hrac.grid(row=0,column=3,padx=5)

ttk.Label(form_vys,text="Skóre:").grid(row=0,column=4,padx=5)
e_skore = tk.Entry(form_vys,width=10, bg="white")
e_skore.grid(row=0,column=5,padx=5)
placeholder(e_skore,"např. 150")

tree_vys = ttk.Treeview(frame_vys, columns=("id","hra","hrac","skore"), show="headings")
for c,t in zip(("id","hra","hrac","skore"), ("ID","Hra","Hráč","Skóre")):
    tree_vys.heading(c, text=t)
    tree_vys.column(c, anchor="center")
tree_vys.pack(fill="both", expand=True, pady=10)

# ======= Funkce pro VÝSLEDKY =======
def load_combos():
    cursor.execute("SELECT id,nazev FROM hry")
    cb_hra["values"] = [f"{i} - {n}" for i,n in cursor.fetchall()]
    cursor.execute("SELECT id,prezdivka FROM hraci")
    cb_hrac["values"] = [f"{i} - {p}" for i,p in cursor.fetchall()]

def load_vys():
    tree_vys.delete(*tree_vys.get_children())
    cursor.execute("""
        SELECT vysledky.id, hry.nazev, hraci.prezdivka, vysledky.skore
        FROM vysledky
        JOIN hry ON hry.id=vysledky.hra_id
        JOIN hraci ON hraci.id=vysledky.hrac_id
        ORDER BY vysledky.skore DESC
    """)
    for r in cursor.fetchall():
        tree_vys.insert("", "end", values=r)

def select_vys(e):
    global selected_vys_id
    item = tree_vys.item(tree_vys.selection())
    if item["values"]:
        selected_vys_id = item["values"][0]
        e_skore.delete(0,"end")
        e_skore.insert(0,item["values"][3])
        e_skore.config(foreground="black")

tree_vys.bind("<<TreeviewSelect>>", select_vys)

def add_vys():
    cursor.execute("INSERT INTO vysledky (hra_id,hrac_id,skore) VALUES (?,?,?)",
                   (cb_hra.get().split(" - ")[0], cb_hrac.get().split(" - ")[0], int(e_skore.get())))
    conn.commit()
    load_vys()

def update_vys():
    cursor.execute("UPDATE vysledky SET skore=? WHERE id=?", (int(e_skore.get()), selected_vys_id))
    conn.commit()
    load_vys()

def delete_vys():
    cursor.execute("DELETE FROM vysledky WHERE id=?", (selected_vys_id,))
    conn.commit()
    load_vys()

btns_vys = ttk.Frame(frame_vys)
btns_vys.pack(pady=5)
ttk.Button(btns_vys,text="➕ Přidat",command=add_vys).grid(row=0,column=0,padx=5)
ttk.Button(btns_vys,text="✏️ Upravit",command=update_vys).grid(row=0,column=1,padx=5)
ttk.Button(btns_vys,text="🗑️ Smazat",command=delete_vys).grid(row=0,column=2,padx=5)

load_combos()
load_vys()

root.mainloop()
