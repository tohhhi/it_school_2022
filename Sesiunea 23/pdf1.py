import pathlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")

MIN_Y = -24


def draw_seller(c, name, address):
    y_start = A4[1] - 12
    c.drawString(0, y_start, "Vanzator")
    c.drawString(0, y_start - 12, f"Nume: {name}")
    c.drawString(0, y_start - 24, f"Adresa: {address}")



def draw_buyer(c, name, address):
    y_start = A4[1] - 12
    x_start = A4[0] - 100
    c.drawString(x_start, y_start, "Cumparator")
    c.drawString(x_start, y_start - 12, f"Nume: {name}")
    c.drawString(x_start, y_start - 24, f"Adresa: {address}")

# 1. creem canvas - spatiu de lucru
canv = canvas.Canvas(str(files_path.joinpath("hello.pdf")))

# schimbam originea
canv.translate(0, A4[1] - 20)



# 2. desenam ce avem nevoie

# draw_buyer(canv, "Mihai Dinu", "Bucuresti")
draw_seller(canv, "eMag", "Bucuresti")
canv.setFillColorRGB(0.1, 0.1, 0.1)
canv.rect(0, -30, 100, 50, fill=True)

# 3. salvam pagina
canv.showPage()


# 4. mai adaugam ceva contiut
# canv.drawString(0, 0, "Origin")

# 5. salvam pagina
# canv.showPage()


# 6. salvam decoument
canv.save()