
import sys
import os
import sqlite3
import pathlib


ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("todo.db")

db_con = sqlite3.connect(DB_FILE)

sw_name = "TO DO APP"

def create_to_do_table(connection):
    cur = connection.cursor()
    
    cur.execute("""
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
)
""")

    connection.commit()

def add_to_do(text):
    cur = db_con.cursor()
    
    cur.execute("""INSERT INTO todo (text) VALUES (?)""",(text,))

    db_con.commit()


def show_to_do():
    cur = db_con.cursor()

    rows = cur.execute("SELECT * FROM todo")

    db_con.commit()

    for i in rows:
        state = "not done"
        if i[2] != 0:
            state = "done"
        
        print(f"[{state}] {i[0]} {i[1]}")

    input("Press any key:")

def resolve_to_do(id):
    cur = db_con.cursor()

    cur.execute("UPDATE todo SET done = 1 WHERE id=?",(id,))
    

    db_con.commit()

def add_to_do_flow():
    text = input("Text to do:")
    add_to_do(str(text))

def show_to_do_flow():
    show_to_do()

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
        1: {"text": "Adauga to do.", "f": add_to_do_flow},
        2: {"text": "Vezi to do.", "f": show_to_do_flow},
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

