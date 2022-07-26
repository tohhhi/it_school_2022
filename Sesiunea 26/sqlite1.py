import sqlite3
import pathlib





ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("dev.db")

# 1. Conectarea la baza de date:
con = sqlite3.connect(DB_FILE)

# 2. Creeare cursor:

cur = con.cursor()

# 3. Compunere QUERY (interogare baza de date):

# Creare tabel

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE
)
""")

cur.execute("""
INSERT INTO contacts (first_name, last_name, phone)
VALUES
("Andrei", "Mihalcea", "0873432452"),
("Ionut", "Mincu", "0738384839")
""")

# 4. Commit - executarea QUERY:
con.commit()