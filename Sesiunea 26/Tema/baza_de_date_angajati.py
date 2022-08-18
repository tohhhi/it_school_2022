import sys
import os
import sqlite3
import pathlib
import csv
import pandas as pd

FILES_DIR = pathlib.Path(__file__).parent.joinpath("files")



ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("salariati.db")


db_con = sqlite3.connect(DB_FILE)

sw_name = "HOMEWORK APP"

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
    
            cur.execute("""INSERT INTO angajati (nume,prenume,salariu_brut) VALUES (?,?,?)""",(row[1],row[0],row[2]))

    

            db_con.commit()
                

def sql_to_csv(sql_table):



    cur = db_con.cursor()

    rows = cur.execute(f"SELECT * FROM {sql_table}") # rows = generator care trebuie transf. intr-o lista sau iterat direct.

    row_list = list(rows)
    user = []

    for i in row_list:
        user.append(f"{i[1]},{i[2]},{i[3]}")
        
    db_con.commit()

    db_con.close()

    rows = [user[0], user[1], user[2]]
            
    # name of csv file 
    filename = os.path.join('C:\\Users\\tohan\\Desktop\\IT-SCHOOL\\Sesiunea 26\\Tema', 'salary.csv')
        
    # writing to csv file 
    write_to_file = open(filename, 'w') 
    
    write_to_file.writelines('\n'.join(user))

    write_to_file.close()




def import_from_csv_flow():
    path = input("Adaugati calea catre csv:")
    csv_to_sql(path)

def export_sql_table_to_csv_flow():
    sql_table = input("Adaugati numele tabelului sql.")
    sql_to_csv(sql_table)

def pdf_generator_from_csv_flow():
    csv_file = input("Adaugati nume csv.")
    


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
        3: {"text": "Genereaza fluturasi salariu.", "f": pdf_generator_from_csv_flow},
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
    create_table_angajati(con)

    while True:
        
        print_banner(sw_name)
        current_flow = get_main_menu_choice()
        # call user choice flow
        current_flow()


if __name__ == "__main__":
    main()

