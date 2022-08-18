import sqlite3
import pathlib
import csv
import os 

ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("salariati.db")

con = sqlite3.connect(DB_FILE)

def sql_to_csv(sql_table):



    cur = con.cursor()

    rows = cur.execute(f"SELECT * FROM {sql_table}") # rows = generator care trebuie transf. intr-o lista sau iterat direct.

    row_list = list(rows)
    user = []

    for i in row_list:
        user.append(f"{i[1]},{i[2]},{i[3]}")
        
    con.commit()

    con.close()

    rows = [user[0], user[1], user[2]]
            
    # name of csv file 
    filename = os.path.join('C:\\Users\\tohan\\Desktop\\IT-SCHOOL\\Sesiunea 26\\Tema', 'salary.csv')
        
    # writing to csv file 
    write_to_file = open(filename, 'w') 
    
    write_to_file.writelines('\n'.join(user))

    write_to_file.close()



