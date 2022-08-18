import sqlite3
import pathlib

ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("test.db")



class Menu:

    @staticmethod
    def add_car_menu():
        return {
            "marca": input("Adauga marca:"),
            "model": input("Adauga model:"),
            "an_fabricatie": input("Adauga an fabricatie:"),
            "tip_caroserie": input("Adauga tipul caroseriei:"),
            "serie_sasiu": input("Adauga serie sasiu:"),
            "numar_inmatriculare": input("Adauga numarul de inmatriculare:")
        }

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

    @staticmethod
    def add_rezervari_menu():
        return {
            "data_start": input("Data:"),
            "perioada": input("Adauga perioada dorita:"),
            "client_id": input("Adauga id-ul unui client:"),
            "car_id": input("Adauga id-ul unei masini:")
        }


class DataBase:
    def __init__(self, connection):
        self.conn = sqlite3.connect(connection)
        
        

    def create_car_table(self):

        self.conn.cursor()

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS masini (
            id INTEGER PRIMARY KEY,
            marca TEXT NOT NULL,
            model TEXT NOT NULL,
            an_fabricatie INTEGER NOT NULL,
            tip_caroserie TEXT NOT NULL,
            serie_sasiu TEXT NOT NULL,
            numar_inmatriculare TEXT NOT NULL
        )
            """)

        self.conn.commit()





    def create_client_table(self):

        self.conn.cursor()

        self.conn.execute("""
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

        self.conn.commit()

    def create_rezervari_table(self):

        self.conn.cursor()

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS rezervari (
            id INTEGER PRIMARY KEY,
            data_start DATE,
            perioada INTEGER,
            client_id INTEGER, 
            car_id INTEGER,
            FOREIGN KEY (client_id) REFERENCES clienti(id),
            FOREIGN KEY (car_id) REFERENCES masini(id)
        )
            """)


        # FOREIGN KEY (clienti_id) REFERENCES clienti(id),
        # FOREIGN KEY (masini_id) REFERENCES masini(id) 
        # FK car id 
        # FK client id  

        self.conn.commit()


    def insert_into_clienti(self, client_data):

        self.conn.cursor()

        self.conn.execute("""INSERT INTO clienti (nume, prenume, cnp, adresa, telefon, email) VALUES (?,?,?,?,?,?)""",(client_data["nume"], client_data["prenume"], client_data["cnp"], client_data["adresa"], client_data["telefon"], client_data["email"]))

        self.conn.commit()

    def insert_into_car(self, car_data):
        
        self.conn.cursor()

        self.conn.execute("""INSERT INTO masini (marca, model, an_fabricatie, tip_caroserie, serie_sasiu, numar_inmatriculare) VALUES (?,?,?,?,?,?)""",(car_data["marca"], car_data["model"], car_data["an_fabricatie"], car_data["tip_caroserie"], car_data["serie_sasiu"], car_data["numar_inmatriculare"]))

        self.conn.commit()

    def insert_into_rezervari(self, rezervari_data):
        
        self.conn.cursor()

        self.conn.execute("""INSERT INTO rezervari (data_start,perioada,client_id,car_id) VALUES (?,?,?,?)""",(rezervari_data["data_start"] , rezervari_data["perioada"], rezervari_data["client_id"], rezervari_data["car_id"]))

        self.conn.commit()

    
    
        
        

class Client:

    def __init__(self, user_data):
        self.__nume = user_data["nume"]
        self.__prenume = user_data["prenume"]
        self.__cnp = user_data["cnp"]
        self.__adresa = user_data["adresa"]
        self.__telefon = user_data["telefon"]
        self.__email = user_data["email"]

 
    
class Car:

    def __init__(self, car_data):
        self.__marca = car_data["marca"]
        self.__model = car_data["model"]
        self.__an_fabricatie = car_data["an_fabricatie"]
        self.__tip_caroserie = car_data["tip_caroserie"]
        self.__serie_sasiu = car_data["serie_sasiu"]
        self.__numar_inmatriculare = car_data["numar_inmatriculare"]

            
class Rezervari:
    
    def __init__(self, rezervari_data):
        self.__perioada_rezervare = rezervari_data["data_start"]
        self.__rezervat = rezervari_data["perioada"]
        self.__rezervat = rezervari_data["client_id"]
        self.__rezervat = rezervari_data["car_id"]
        




make_table = DataBase(DB_FILE)

make_table.create_client_table()

make_table.create_car_table()

make_table.create_rezervari_table()

user_input = Menu.add_client_menu()

car_input = Menu.add_car_menu()

rezervare_input = Menu.add_rezervari_menu()

car1 = Car(car_input)

user1 = Client(user_input)

rezervare1 = Rezervari(rezervare_input)


make_table.insert_into_clienti(user_input)

make_table.insert_into_car(car_input)


make_table.insert_into_rezervari(rezervare_input)




# mereu data de azi cu datetime

# cand incepe fuluxul 3 arat lista cu masini 
# listeaza toti clientii
# alege id client
# arata lista de masini nerezervate
# alege lista de masini 
