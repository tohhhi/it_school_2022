import sqlite3
import pathlib
import sys
import datetime
import logging


ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("car_rental.db")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
    )


class Menu:    

    @staticmethod
    def add_cars_flow():
        make_table.create_cars_table()
        make_table.create_customers_table()
        make_table.create_reservations_table()

        car_input = Menu.add_car_menu()

        make_table.insert_into_cars(car_input)

    @staticmethod
    def add_customers_flow():

        user_input = Menu.add_customer_menu()

        make_table.insert_into_customers(user_input)

    @staticmethod
    def add_reservations_flow():
        print("------Cars------")
        make_table.show_cars()
        print("------Customers------")
        make_table.show_customers()

        reservations_input = Menu.add_reservations_menu()

        make_table.insert_into_reservations(reservations_input)

    @staticmethod
    def print_reservations_flow():
        make_table.show_cars_reservations()

    @staticmethod
    def delete_reservations_flow():
        make_table.print_reservations()
        reservations_id = input("Add the id of the reservations you want to delete:")
        make_table.delete_reservations(reservations_id)
    
    @staticmethod
    def get_main_menu_choice():

        
        choice_ok = False
        m_menu_entries = {
            1: {"text": "Add a car.", "f": Menu.add_cars_flow},
            2: {"text": "Add a customer.", "f": Menu.add_customers_flow},
            3: {"text": "Add a reservation.", "f": Menu.add_reservations_flow},
            4: {"text": "Show reservations.", "f": Menu.print_reservations_flow},
            5: {"text": "Cancel reservation.", "f": Menu.delete_reservations_flow},
            0: {"text": "Close the program.", "f": sys.exit}
        }

        while not choice_ok:
            for k, v in m_menu_entries.items():
                print(k, ". ", v["text"], sep="")
            choice = input("\nChoose an option: ")
            if not choice.isnumeric() or int(choice) not in m_menu_entries.keys():
                logging.error("Please choose a number from the list below.\n\n")
            else:
                choice_ok = True

        return m_menu_entries[int(choice)]["f"]

    @staticmethod
    def add_car_menu():
        return {
            "Brand": input("Add car brand:"),
            "Model": input("Add car model:"),
            "Year": input("Add year of manufacture:"),
            "Car_body": input("Add body type:"),
            "Chassis_series": input("Add chassis series:"),
            "Registration_number": input("Add registration number:")
        }

    @staticmethod
    def add_customer_menu():
        return {
            "Last_name": input("Add last name:"),
            "First_name": input("Add first name:"),
            "Personal_number": input("Add personal identification number:"),
            "Adress": input("Add your addres:"),
            "Phone": input("Add your phone number:"),
            "Email": input("Add your email:")
        }

    @staticmethod
    def add_reservations_menu():
        return {
            "Data_start": input("Date:"),
            "Period": input("Add the period:"),
            "Customer_id": input("Add a client_id:"),
            "Car_id": input("Add a car id:")
        }


class DataBase:
    def __init__(self, connection):
        self.conn = sqlite3.connect(connection)
        
    def create_cars_table(self):

        self.conn.cursor()

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY,
            Brand TEXT NOT NULL,
            Model TEXT NOT NULL,
            Year INTEGER NOT NULL,
            Car_body TEXT NOT NULL,
            Chassis_series TEXT NOT NULL,
            Registration_number TEXT NOT NULL
        )
            """)

        self.conn.commit()

    def create_customers_table(self):

        self.conn.cursor()

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            Last_name TEXT NOT NULL,
            First_name TEXT NOT NULL,
            Personal_number INTEGER NOT NULL,
            Adress TEXT NOT NULL,
            Phone TEXT NOT NULL,
            Email TEXT NOT NULL 
        )
            """)

        self.conn.commit()

    def create_reservations_table(self):

        self.conn.cursor()

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY,
            Data_start DATE,
            Period INTEGER,
            Customer_id INTEGER UNIQUE, 
            Car_id INTEGER UNIQUE,
            FOREIGN KEY (Customer_id) REFERENCES customers(id),
            FOREIGN KEY (Car_id) REFERENCES cars(id)
        )
            """)

        self.conn.commit()

    def insert_into_customers(self, customer_data):

        self.conn.cursor()

        self.conn.execute("""INSERT INTO customers (Last_name, First_name, Personal_number, Adress, Phone, Email) VALUES (?,?,?,?,?,?)""",(customer_data["Last_name"], customer_data["First_name"], customer_data["Personal_number"], customer_data["Adress"], customer_data["Phone"], customer_data["Email"]))

        self.conn.commit()

    def insert_into_cars(self, car_data):
        
        self.conn.cursor()

        self.conn.execute("""INSERT INTO cars (Brand, Model, Year, Car_body, Chassis_series, Registration_number) VALUES (?,?,?,?,?,?)""",(car_data["Brand"], car_data["Model"], car_data["Year"], car_data["Car_body"], car_data["Chassis_series"], car_data["Registration_number"]))

        self.conn.commit()

    
    def insert_into_reservations(self, reservations_data):
        try:
            self.conn.cursor()

            self.conn.execute("""INSERT INTO reservations (Data_start, Period, Customer_id, Car_id) VALUES (?,?,?,?)""",(reservations_data["Data_start"] , reservations_data["Period"], reservations_data["Customer_id"], reservations_data["Car_id"]))

            self.conn.commit()
        except sqlite3.IntegrityError as err:
            logging.warning("The car is already booked.")

    def print_reservations(self):

        cur = self.conn.cursor()

        rows = cur.execute("SELECT * FROM reservations")

        row_list = list(rows)

        for i in row_list:
            print(f"Reservations_id: {i[0]} | Data_start: {i[1]} | Period: {i[2]} days | Client_id: {i[3]} | Car_id: {i[4]}")

        self.conn.commit()

    def delete_reservations(self, id):
        sql = 'DELETE FROM reservations WHERE id=?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()
    
    def show_cars(self):
        
        cur = self.conn.cursor()

        rows = cur.execute("SELECT * FROM cars")

        row_list = list(rows)

        for i in row_list:
            print(f"Car_id: {i[0]} | Car_brand: {i[1]} | Registration_number: {i[6]}")

        self.conn.commit()

    def show_customers(self):
        
        cur = self.conn.cursor()

        rows = cur.execute("SELECT * FROM customers")

        row_list = list(rows)

        for i in row_list:
            print(f"Client_id: {i[0]} | Last name: {i[1]} | First name: {i[2]}")

        self.conn.commit()

    def show_cars_reservations(self):
        cur = self.conn.cursor()
    
        
        rows = cur.execute("""
        SELECT Registration_number, car_id
        FROM reservations
        INNER JOIN cars ON cars.id = reservations.id;
        """)

        row_list = list(rows)

        for i in row_list:
            print(f"Car_id: {i[1]} | Registration_number: {i[0]}")

        self.conn.commit()
    
    def verify_reservations(self):
        
        cur = self.conn.cursor()
    
        rows = cur.execute("SELECT * FROM reservations")

        row_list = list(rows)

        for i in row_list:
            
            today = datetime.datetime.today() 
            
            date_1 = datetime.datetime.strptime(i[1], "%d.%m.%Y")

            end_date = date_1 + datetime.timedelta(days=i[2])
            
            if today >= end_date:
                sql = 'DELETE FROM reservations WHERE Data_start=?'
                cur = self.conn.cursor()
                cur.execute(sql, (i[1],))
                self.conn.commit()

class Client:

    def __init__(self, user_data):
        self.__last_name = user_data["Last_name"]
        self.__first_name = user_data["First_name"]
        self.__personal_number = user_data["Personal_number"]
        self.__adress = user_data["Adress"]
        self.__phone = user_data["Phone"]
        self.__email = user_data["Email"]
 
class Car:

    def __init__(self, car_data):
        self.__brand = car_data["Brand"]
        self.__model = car_data["Model"]
        self.__year = car_data["Year"]
        self.__car_body = car_data["Car_body"]
        self.__chassis_series = car_data["Chassis_series"]
        self.__registration_number = car_data["Registration_number"]

            
class Rezervari:
    
    def __init__(self, reservations_data):
        self.__data_start = reservations_data["Data_start"]
        self.__period = reservations_data["Period"]
        self.__client_id = reservations_data["Customer_id"]
        self.__car_id = reservations_data["Car_id"]
        
make_table = DataBase(DB_FILE)

menu1 = Menu()

logging.info("Hello! Script is starting...")
while True:
    car_menu_choose = menu1.get_main_menu_choice()
    car_menu_choose()
    try:
        make_table.verify_reservations()
    except TypeError as err:
        logging.error("The format of the date need to be: 'day.month.year'.")


