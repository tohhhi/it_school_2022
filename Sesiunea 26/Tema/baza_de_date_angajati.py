import sys
import os
import sqlite3
import pathlib
import pandas 
import pandas as pd



ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("salariati.db")


db_con = sqlite3.connect(DB_FILE)

sw_name = "HOMEWORK APP"

def create_to_do_table(connection):
    cur = connection.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS salariati (
        id INTEGER PRIMARY KEY,
        prenume TEXT NOT NULL,
        nume TEXT NOT NULL,
        salariu_brut TEXT NOT NULL UNIQUE
    )
    """)

    connection.commit()

def import_from_csv(path):
    
    df = pandas.read_csv(path)
    
    cur = db_con.cursor()
    
    for row in df.itertuples():
        cur.execute('''
                    INSERT INTO salariati (prenume, nume, salariu_brut)
                    VALUES (?,?,?)
                    ''',(row.Prenume,row.Nume,row.Salariu_brut))
                

    db_con.commit()


def import_to_csv(sql_table):
    con = sqlite3.connect(DB_FILE)

    sql_query = pd.read_sql_query(f"select * from {sql_table}",con)


    sql_query.to_csv("salariu.csv")

def resolve_to_do(id):
    cur = db_con.cursor()

    cur.execute("UPDATE todo SET done = 1 WHERE id=?",(id,))
    

    db_con.commit()

def import_from_csv_flow():
    path = input("Adaugati calea catre csv:")
    import_from_csv(path)

def export_sql_table_to_csv_flow():
    sql_table = input("Adaugati numele tabelului sql.")
    import_to_csv(sql_table)

def resolve_to_do_flow():
    to_do_id = int(input("Id to do:"))
    resolve_to_do(to_do_id)


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner(title):
    """Prints program banner."""

    cls()
    print("+", "-" * (len(title) + 2), "+", sep="")
    print("|", title, "|")
    print("+", "-" * (len(title) + 2), "+", sep="")

def get_main_menu_choice():
    """Show main menu items asking the user for a choice.
    Returns the function to call next based on user choice.
    """
    choice_ok = False
    m_menu_entries = {
        1: {"text": "Importa din csv.", "f": import_from_csv_flow},
        2: {"text": "Exporta din sql table in csv.", "f": export_sql_table_to_csv_flow},
        3: {"text": "Rezolva to do.", "f": resolve_to_do_flow},
        0: {"text": "Inchide program.", "f": sys.exit},
    }

    while not choice_ok:
        for k, v in m_menu_entries.items():
            print(k, ". ", v["text"], sep="")
        choice = input("\nAlege un numar: ")
        if not choice.isnumeric() or int(choice) not in m_menu_entries.keys():
            cls()
            print("EROARE: Te rog sa alegi un numar din lista de mai jos.\n\n")
        else:
            choice_ok = True

    return m_menu_entries[int(choice)]["f"]


def main():
    con = sqlite3.connect(DB_FILE)
    create_to_do_table(con)

    while True:
        
        print_banner(sw_name)
        current_flow = get_main_menu_choice()
        # call user choice flow
        current_flow()


if __name__ == "__main__":
    main()

