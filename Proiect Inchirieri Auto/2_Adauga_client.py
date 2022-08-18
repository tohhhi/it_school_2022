import sqlite3
import pathlib

ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("clienti.db")
db_con = sqlite3.connect(DB_FILE)


def create_client_table(connection):

        cur = connection.cursor()

        cur.execute("""
    CREATE TABLE IF NOT EXISTS clienti (
        id INTEGER PRIMARY KEY,
        nume TEXT NOT NULL,
        prenume TEXT NOT NULL,
        cnp INTEGER NOT NULL,
        adresa TEXT NOT NULL,
        telefon INTEGER NOT NULL,
        email TEXT NOT NULL 
    )
        """)

        connection.commit()


create_client_table(db_con)



class Client:




    def __init__(self, user_data):
        self.__nume = user_data["nume"]
        self.__prenume = user_data["prenume"]
        self.__cnp = user_data["cnp"]
        self.__adresa = user_data["adresa"]
        self.__telefon = user_data["telefon"]
        self.__email = user_data["email"]



    def insert_into_db(self):
        cur = db_con.cursor()

        cur.execute("""INSERT INTO clienti (nume, prenume, cnp, adresa, telefon, email) VALUES (?,?,?,?,?,?)""",(self.__nume, self.__prenume, self.__cnp, self.__adresa, self.__telefon, self.__email))

        db_con.commit()


    



# user1 = Client()


class Menu:

    @staticmethod
    def add_client_menu():
        return {
            "nume": input("Adauga nume:"),
            "prenume": input("Adauga prenume:"),
            "cnp": input("Adauga cnp:"),
            "adresa": input("Adauga adresa:"),
            "telefon": input("Adauga numar de telefon:"),
            "email": input("Adauga email:")
        }


  

user_input = Menu.add_client_menu()

user1 = Client(user_input)

user1.insert_into_db() 

print(user_input)