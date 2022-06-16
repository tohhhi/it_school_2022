class Pen:

    # atribut de clasa
    brand = "NOKI"
    
    
    def __init__(self, color):
        self.color = color
        self.is_empty = False



pen = Pen("red")
pen2 = Pen("black")

print(pen.brand)
print(pen2.brand)

# pen2.owner = "Mihai"

# print(pen2.owner)

pen2.brand = "pen2-brand" # creeaza un atribut de instanta pt ca nu are voie sa modifice atributul static

print(Pen.brand)

#print(pen.color)
#print(pen2.color)

#print(Pen.brand)

#print(pen.brand)


