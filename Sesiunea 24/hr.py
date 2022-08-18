import csv
import pathlib
from fluturas_gen import generate

FILES_DIR = pathlib.Path(__file__).parent.joinpath("files")

try:
    with open(FILES_DIR.joinpath('salarii.csv')) as fin:
        reader = csv.reader(fin)
        for line in reader:
            full_name = f"{line[0]} {line[1]}"
            full_name = full_name
            generate(full_name, float(line[3]), int(line[4]))
except OSError:
    print("Error opening salarii.csv.")