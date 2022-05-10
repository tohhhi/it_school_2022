# 1. Scrie un program care citeste de la tastatura un numar 
# natural si afiseaza "Par" daca numarul este par sau "Impar" 
# daca numarul este impar.


number = input("Introdu un numar: ")

number = int(number)

if number % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")