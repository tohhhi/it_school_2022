import sqlite3
import pathlib
import pandas



df = pandas.read_csv('salarii.csv')



ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("angajati.db")

# 1. Conectarea la baza de date:
con = sqlite3.connect(DB_FILE)

# 2. Creeare cursor:

cur = con.cursor()

# 3. Compunere QUERY (interogare baza de date):

# Creare tabel

cur.execute("""
CREATE TABLE IF NOT EXISTS angajati (
    id INTEGER PRIMARY KEY,
    prenume TEXT NOT NULL,
    nume TEXT NOT NULL,
    salariu_brut TEXT NOT NULL UNIQUE
)
""")



for row in df.itertuples():
    cur.execute('''
                INSERT INTO angajati (prenume, nume, salariu_brut)
                VALUES (?,?,?)
                ''',(row.Prenume,row.Nume,row.Salariu_brut))
              



# cur.execute("""INSERT INTO angajati (prenume) VALUES (?)""",(prenume,))

# cur.execute("""
# INSERT INTO angajati (prenume, nume, salariu_brut)
# VALUES
# ("Andrei", "Mihalcea", "6000"),
# ("Ionut", "Mincu", "5000")
# """)

# 4. Commit - executarea QUERY:
con.commit()
        



def import_from_csv(path):
    
    df = pandas.read_csv(path)



    ROOT = pathlib.Path(__file__).parent
    DB_FILE = ROOT.joinpath("angajati.db")

    # 1. Conectarea la baza de date:
    con = sqlite3.connect(DB_FILE)

    # 2. Creeare cursor:

    cur = con.cursor()

    # 3. Compunere QUERY (interogare baza de date):

    # Creare tabel

    cur.execute("""
    CREATE TABLE IF NOT EXISTS angajati (
        id INTEGER PRIMARY KEY,
        prenume TEXT NOT NULL,
        nume TEXT NOT NULL,
        salariu_brut TEXT NOT NULL UNIQUE
    )
    """)



    for row in df.itertuples():
        cur.execute('''
                    INSERT INTO angajati (prenume, nume, salariu_brut)
                    VALUES (?,?,?)
                    ''',(row.Prenume,row.Nume,row.Salariu_brut))
                



    # 4. Commit - executarea QUERY:
    con.commit()