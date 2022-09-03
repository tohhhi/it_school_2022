import sqlite3
import pathlib
import sys
import datetime
import logging


ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("test.db")

logging.basicConfig(
    #filename="log.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
    )



class Menu:

    @staticmethod
    def add_cars_flow():
        
        car_input = Menu.add_car_menu()

        make_table.insert_into_car(car_input)

    @staticmethod
    def add_customers_flow():

        user_input = Menu.add_client_menu()

        make_table.insert_into_clienti(user_input)

    @staticmethod
    def add_reservations_flow():
        print("------Cars------")
        make_table.show_cars()
        print("------Customers------")
        make_table.show_customers()

        reservations_input = Menu.add_rezervari_menu()

        make_table.insert_into_rezervari(reservations_input)

    @staticmethod
    def print_reservations_flow():
        make_table.show_rezervari_masina()

    @staticmethod
    def delete_reservations_flow():
        id_rezervare = input("Adauga id-ul rezervarii pe care vrei sa o anulezi:")
        make_table.anuleaza_rezervare(id_rezervare)
    


    @staticmethod
    def get_main_menu_choice():

        
        choice_ok = False
        m_menu_entries = {
            1: {"text": "Adauga masina.", "f": Menu.add_cars_flow},
            2: {"text": "Adauga client.", "f": Menu.add_customers_flow},
            3: {"text": "Adauga rezervare.", "f": Menu.add_reservations_flow},
            4: {"text": "Vezi rezervari.", "f": Menu.print_reservations_flow},
            5: {"text": "Anuleaza rezervare.", "f": Menu.delete_reservations_flow},
            0: {"text": "Inchide programul.", "f": sys.exit}
        }

        while not choice_ok:
            for k, v in m_menu_entries.items():
                print(k, ". ", v["text"], sep="")
            choice = input("\nAlege un numar: ")
            if not choice.isnumeric() or int(choice) not in m_menu_entries.keys():
                logging.error("Te rog sa alegi un numar din lista de mai jos.\n\n")
            else:
                choice_ok = True

        return m_menu_entries[int(choice)]["f"]
    
    

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
            telefon TEXT NOT NULL,
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
                client_id INTEGER UNIQUE, 
                car_id INTEGER UNIQUE,
                FOREIGN KEY (client_id) REFERENCES clienti(id),
                FOREIGN KEY (car_id) REFERENCES masini(id)
            )
                """)

            self.conn.commit()
        



    def insert_into_clienti(self, client_data):

        self.conn.cursor()
        if len(client_data["cnp"]) == 13:
            self.conn.execute("""INSERT INTO clienti (nume, prenume, cnp, adresa, telefon, email) VALUES (?,?,?,?,?,?)""",(client_data["nume"], client_data["prenume"], client_data["cnp"], client_data["adresa"], client_data["telefon"], client_data["email"]))
        else:
            logging.info("CNP TRB SA AIBA 10 caractere.")
        self.conn.commit()

    def insert_into_car(self, car_data):
        
        self.conn.cursor()

        self.conn.execute("""INSERT INTO masini (marca, model, an_fabricatie, tip_caroserie, serie_sasiu, numar_inmatriculare) VALUES (?,?,?,?,?,?)""",(car_data["marca"], car_data["model"], car_data["an_fabricatie"], car_data["tip_caroserie"], car_data["serie_sasiu"], car_data["numar_inmatriculare"]))

        self.conn.commit()

    def insert_into_rezervari(self, rezervari_data):
        try:
            self.conn.cursor()

            self.conn.execute("""INSERT INTO rezervari (data_start,perioada,client_id,car_id) VALUES (?,?,?,?)""",(rezervari_data["data_start"] , rezervari_data["perioada"], rezervari_data["client_id"], rezervari_data["car_id"]))

            self.conn.commit()
        except sqlite3.IntegrityError as err:
            logging.warning("Masina este deja rezervata.")
            # print("***WARNING***")
            # print("Masina este deja rezervata!!!")
            # print("Te rugam adauga un id de masina diponibil:")

    def print_rezervari(self):
        
        cur = self.conn.cursor()

        rows = cur.execute("SELECT * FROM rezervari")

        row_list = list(rows)

        for i in row_list:
            print(f"id_rezervare: {i[0]} | data_start: {i[1]} | perioada: {i[2]} zile | client_id: {i[3]} | car_id: {i[4]}")

        self.conn.commit()

    # cand incepe fuluxul 3 arat lista cu masini 
    def show_cars(self):
        
        cur = self.conn.cursor()

        rows = cur.execute("SELECT * FROM masini")

        row_list = list(rows)

        for i in row_list:
            print(f"id_masina: {i[0]} | marca_masina: {i[1]} | numar_inmatriculare: {i[6]}")

        self.conn.commit()
        
    # listeaza toti clientii
    def show_customers(self):
        
        cur = self.conn.cursor()

        rows = cur.execute("SELECT * FROM clienti")

        row_list = list(rows)

        for i in row_list:
            print(f"id_client: {i[0]} | Nume: {i[1]} | Prenume: {i[2]}")

        self.conn.commit()
        
    def anuleaza_rezervare(self, id):
        sql = 'DELETE FROM rezervari WHERE id=?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    
    def show_rezervari_masina(self):
        cur = self.conn.cursor()
    
        
        rows = cur.execute("""
        SELECT numar_inmatriculare, car_id
        FROM rezervari
        INNER JOIN masini ON masini.id = rezervari.id;
        """)

        row_list = list(rows)

        for i in row_list:
            print(f"car_id: {i[1]} | numar_inmatriculare: {i[0]}")

        self.conn.commit()
        

        

    
    def expirare_rezervare(self):
        
        cur = self.conn.cursor()
    
        
        rows = cur.execute("SELECT * FROM rezervari")

        row_list = list(rows)

       

        for i in row_list:
            
            today = datetime.datetime.today() #.strftime("%d.%m.%Y")

            #print(today)

            
            date_1 = datetime.datetime.strptime(i[1], "%d.%m.%Y")

            end_date = date_1 + datetime.timedelta(days=i[2])
            # print(type(today))
            # print(type(end_date))

            if today >= end_date:
                sql = 'DELETE FROM rezervari WHERE data_start=?'
                cur = self.conn.cursor()
                cur.execute(sql, (i[1],))
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

# menu1 = Menu()
try:
    conn2 = sqlite3.connect(DB_FILE)


    c = conn2.cursor()

    #get the count of tables with the name
    c.execute(""" SELECT count(*) FROM rezervari """)

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : 
        logging.info("Program functional")
        menu1 = Menu()   
    else:
        logging.critical("Tabelul rezervari nu exista dar a fost creat.")
        make_table.create_rezervari_table()
        menu1 = Menu()
        
        

    #commit the changes to db
    conn2.commit()
    #close the connection
    conn2.close()

except sqlite3.Error as error:
    logging.critical("Error while connecting to sqlite")         

try:
    conn2 = sqlite3.connect(DB_FILE)


    c = conn2.cursor()

    #get the count of tables with the name
    c.execute(""" SELECT count(*) FROM masini """)

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : 
        logging.info("Program functional")
        menu1 = Menu()   
    else:
        logging.critical("Tabelul rezervari nu exista dar a fost creat.")
        make_table.create_rezervari_table()
        menu1 = Menu()
        
        

    #commit the changes to db
    conn2.commit()
    #close the connection
    conn2.close()

except sqlite3.Error as error:
    logging.critical("Error while connecting to sqlite")     

try:
    conn2 = sqlite3.connect(DB_FILE)


    c = conn2.cursor()

    #get the count of tables with the name
    c.execute(""" SELECT count(*) FROM clienti """)

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : 
        logging.info("Program functional")
        menu1 = Menu()   
    else:
        logging.critical("Tabelul rezervari nu exista dar a fost creat.")
        make_table.create_rezervari_table()
        menu1 = Menu()
        
        

    #commit the changes to db
    conn2.commit()
    #close the connection
    conn2.close()

except sqlite3.Error as error:
    logging.critical("Error while connecting to sqlite")     

# make_table.create_client_table()

# make_table.create_car_table()

# make_table.create_rezervari_table()


logging.info("Hello! Script is starting...")
while True:
    car_menu_choose = menu1.get_main_menu_choice()
    car_menu_choose()

# eroare cand nu pot creea baza de date
# cu join la vezi rezervari..

# make_table.expirare_rezervare()
#make_table.show_rezervari_masina()

#make_table.print_rezervari()

# make_table.show_cars()

# make_table.show_customers()

# make_table.anuleaza_rezervare(1)

# make_table.create_client_table()

# make_table.create_car_table()

# make_table.create_rezervari_table()

# user_input = Menu.add_client_menu()

# car_input = Menu.add_car_menu()

# rezervare_input = Menu.add_rezervari_menu()

# car1 = Car(car_input)

# user1 = Client(user_input)

# rezervare1 = Rezervari(rezervare_input)


# make_table.insert_into_clienti(user_input)

# make_table.insert_into_car(car_input)


# make_table.insert_into_rezervari(rezervare_input)




# mereu data de azi cu datetime

# cand incepe fuluxul 3 arat lista cu masini 
# listeaza toti clientii
# alege id client
# arata lista de masini nerezervate
# alege lista de masini 
# if data_start + cate zile < datetime.now