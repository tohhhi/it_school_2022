import csv
from email import header
import pathlib
import pathlib
from openpyxl import Workbook, load_workbook
import pandas as pd




# Reading the csv file
df_new = pd.read_csv('C:\\Users\\tohan\\Desktop\\IT-SCHOOL\\Sesiunea 24\\files\salarii.csv', header=None)
 
# saving xlsx file
GFG = pd.ExcelWriter('Excell_salariati.xlsx')

new_header = ["Prenume","Nume","Id","Salariu","Zile libere"]

df_new.to_excel(GFG, index=False, header=new_header, sheet_name="Tabel_salariati")
 
GFG.save()