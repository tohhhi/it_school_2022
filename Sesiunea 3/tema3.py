# 3. Scrie un program care citeste de la tastatura doua numere, a si b.
# Daca a > b sa se diferenta suma lor.
# Daca a == b sa se afiseze a la puterea b
# Altfel sa se afiseze suma lor.

a = input("a = ")

a = int(a)

b = input("b = ")

b = int(b)

if a > b:
    print(a-b)
elif a == b:
    print(a ** b)
else:
    print(a+b)