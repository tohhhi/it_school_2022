from multiprocessing import connection
import pandas as pd 
import pathlib
import sqlite3


ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("salariati.db")

# con = sqlite3.connect(DB_FILE)

# sql_query = pd.read_sql_query("select * from salariati",con)


# sql_query.to_csv("salariu.csv")



def import_to_csv(sql_table):
    con = sqlite3.connect(DB_FILE)

    sql_query = pd.read_sql_query(f"select * from {sql_table}",con)


    sql_query.to_csv("salariu.csv")


import_to_csv("salariati")
