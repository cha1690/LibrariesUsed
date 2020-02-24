import sqlite3


def connect():
    conn = sqlite3.connect("libraries.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, name text, projectused text, description text)")
    conn.commit()
    conn.close()

def add_entry(name,projectused,description):
    conn = sqlite3.connect("libraries.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO library VALUES (NULL,?,?,?)",(name,projectused,description))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("libraries.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM library")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name,projectused):
    conn = sqlite3.connect("libraries.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM library WHERE name=? OR projectused=?", (name, projectused))
    rows = cur.fetchall()
    conn.close()
    return rows



connect()
add_entry("tkinter","Calcy","hjghjghjghjghgghj")
print(view())