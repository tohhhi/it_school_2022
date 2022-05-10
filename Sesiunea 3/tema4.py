# 4. Scrie un program care citeste de la tastatura doua numere,
# si calculeaza a / b daca a > b sau b / a daca a <= b. Afiseaza 
# rezultatul.

a = input("a = ")

a = int(a)

b = input("b = ")

b = int(b)

if a > b:
    print(a / b)
else:
    print(b / a)
