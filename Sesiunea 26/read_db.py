import sqlite3
import pathlib
import logging

ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("dev.db")

logging.root.setLevel(logging.DEBUG)
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s")

con = sqlite3.connect(DB_FILE)

cur = con.cursor()

rows = cur.execute("SELECT * FROM contacts") # rows = generator care trebuie transf. intr-o lista sau iterat direct.

row_list = list(rows)

for i in row_list:
    print(f"{i[1]} {i[2]} - {i[3]}")

con.commit()




con.close()
