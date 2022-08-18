import sqlite3
import pathlib

ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("Masini.db")
db_con = sqlite3.connect(DB_FILE)


def create_car_table(connection):

        cur = connection.cursor()

        cur.execute("""
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

        connection.commit()


create_car_table(db_con)



class Car:



    def __init__(self):
        self.__marca = input("Adauga marca:")
        self.__model = input("Adauga modelul:")
        self.__an_fabricatie = input("Adauga anul de fabricatie:")
        self.__tip_caroserie = input("Adauga tipul de caroserie:")
        self.__serie_sasiu = input("Adauga serie sasiu:")
        self.__nr_inmatriculare = input("Adauga numarul de inmatriculare:")


    
        cur = db_con.cursor()

        cur.execute("""INSERT INTO masini (marca, model, an_fabricatie, tip_caroserie, serie_sasiu, numar_inmatriculare) VALUES (?,?,?,?,?,?)""",(self.__marca, self.__model, self.__an_fabricatie, self.__tip_caroserie, self.__serie_sasiu, self.__nr_inmatriculare))

        db_con.commit()


    



user1 = Car()









