from csv import reader
from PyPDF2 import PdfReader
import pathlib


root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")



pdf_in = files_path.joinpath("Joshua Bloch - Effective Java (3rd) - 2018.pdf")


reader = PdfReader(pdf_in)

p1 = reader.pages[15]


print(p1.extract_text())


print(reader.numPages)


# https://docs.reportlab.com/reportlab/userguide/ch2_graphics/

# https://jamboard.google.com/d/1Bew-sykZf7nh42M-9s6mFuBiDpVWtUAwUgHR3qkwN3Q/edit?usp=meet_whiteboard

# https://pypdf2.readthedocs.io/en/latest/

