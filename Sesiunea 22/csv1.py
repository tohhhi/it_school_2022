import csv
import pathlib

root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")

# citire fisier csv
try:
    with open(files_path.joinpath("salarii.csv")) as fin:
        reader = list(csv.reader(fin))
except OSError:
    print("File error.")
else:
    lista_salarii = []
    for i in reader:
        
        lista_salarii.append(float(i[3]))

    print(f"Total salarii: {sum(lista_salarii)}")   



# citire fisier csv cu nume campuri
# field_names = [
#     "first_name",
#     "last_name",
#     "id",
#     "gros_salary",
#     "days_off"
# ]
# try:
#     with open(files_path.joinpath("salarii.csv")) as fin:
#         # list -> extrage datele din generator
#         dict_reader = list(csv.DictReader(fin, fieldnames=field_names))
#         for i in dict_reader:
#             print(i)
# except OSError:
#     print("File error.")


# scriere csv
# try:
#     with open(files_path.joinpath("net_salaries.csv"), "w") as fout:
#         csv_writer = csv.writer(fout)
#         for i in reader:
#             net = int(i[3]) * 0.65
#             csv_writer.writerow([i[0], i[1], net])
# except OSError:
#     print("File write error.")

# # csv.DictWriter - get a dict for each line