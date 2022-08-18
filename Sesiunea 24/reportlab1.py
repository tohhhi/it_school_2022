import pathlib
from datetime import datetime
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Frame, Paragraph, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet

files_dir = pathlib.Path(__file__).parent.joinpath("files")

# page padding
PAGE_PADDING = 2 * cm

# 1. create the document, A4 size
canv = Canvas(str(files_dir.joinpath("fluturas.pdf")), pagesize=A4)

# 2. create frames
F1_H = 2 * cm
F1_W = 17 * cm
F1_Y = A4[1] - F1_H - PAGE_PADDING
f1 = Frame(PAGE_PADDING, F1_Y, F1_W, F1_H, showBoundary=1)

F2_H = 6 * cm
F2_W = 17 * cm
F2_Y = F1_Y - F2_H
f2 = Frame(PAGE_PADDING, F2_Y, F2_W, F2_H, showBoundary=1)

F3_Y = F2_Y - F1_H
f3 = Frame(PAGE_PADDING, F3_Y, F1_W / 2, F1_H, showBoundary=1)
f4 = Frame(PAGE_PADDING + F1_W / 2, F3_Y, F1_W / 2, F1_H, showBoundary=1)

# add flowables to frame 1 and paint to canvas
stylesheet = getSampleStyleSheet()
p_style = stylesheet["Heading4"]
p_style.alignment = 1 # centrat
p1 = Paragraph("SC Example SRL", p_style)

p2_style = stylesheet["Normal"]
p2 = Paragraph("Angajat: Dinu Mihai", p2_style)

p3 = Paragraph(f"Generat la: {datetime.now()}", p2_style)

f1.add(p1, canv)
f1.add(p2 , canv)
f1.add(p3, canv)

# add table to frame 2
t_style = TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 0.25, colors.grey)
    ])
matrix = [
    ["Salariu brut:", 5000],
    ["Taxe 45%:", 5000 * 0.45],
    ["Salariu net:", 5000 * 0.65]
]
t1 = Table(matrix, style=t_style, colWidths=F2_W / 2)
f2.add(t1, canv)

# add flowables in frame 3
p_drepturi = Paragraph(f"TOTAL DREPTURI: {5000 * 0.65} RON", stylesheet["Heading5"])
f3.add(p_drepturi, canv)


# add flowables in frame 4
p_bonuri = Paragraph(f"Valoare bonuri de masa: {400} lei", stylesheet["Heading5"])
f4.add(p_bonuri, canv)

# # draw frame borders
f1.drawBoundary(canv)
f2.drawBoundary(canv)
f3.drawBoundary(canv)
f4.drawBoundary(canv)

# # add logo
f5 = Frame(PAGE_PADDING, A4[1] - PAGE_PADDING, F2_W, F1_H)
f5.add(Image(files_dir.joinpath("sears.jpeg"), width=3.3 * cm, height=1 * cm), canv)

# save the document
canv.showPage()
canv.save()

