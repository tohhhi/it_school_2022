import sqlite3
import pathlib
import csv


ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("angajati.db")

db_con = sqlite3.connect(DB_FILE)





def create_table_angajati(connection):
    cur = connection.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS angajati (
        id INTEGER PRIMARY KEY,
        prenume TEXT NOT NULL,
        nume TEXT NOT NULL,
        salariu_brut TEXT NOT NULL UNIQUE
    )
    """)

    connection.commit()

def csv_to_sql(csv_path):

    

    with open(csv_path) as f:
        cf = csv.reader(f)
        
        for row in cf:
            cur = db_con.cursor()
    
            cur.execute("""INSERT INTO angajati (nume,prenume,salariu_brut) VALUES (?,?,?)""",(row[0],row[1],row[2]))

    

            db_con.commit()
            
    
                

    
    

   


# def add_to_do(text):
#     cur = db_con.cursor()
    
#     cur.execute("""INSERT INTO todo (text) VALUES (?)""",(text,))

#     db_con.commit()

create_table_angajati(db_con)

csv_to_sql("C:\\Users\\tohan\\Desktop\\IT-SCHOOL\\Sesiunea 26\\Tema\\salarii.csv")