"""
9. Sa se modifice programul de la pct. 8 astfel:
    - modificam intervalul de generare la [1, 300]
    - in loc de + - o sa afisam dupa cum urmeaza;
    - cand numarul introdus este:
        +/- 50 fata de numarul cautat: "Gheata"   
        +/- 40 fata de numarul cautat: "Frig"
        +/- 30 fata de numarul cautat: "Rece"
        +/- 20 fata de numarul cautat: "Caldut"
        +/- 10 fata de numarul cautat: "Cald"
        +/- 5 fata de numarul cautat: "Frige"
        +/- 2 fata de numarul cautat: "Arde"

    EX:
    Incepe jocul!
    Introduceti un numar intre 1 si 99.
    50
    Caldut
    44
    Caldut
    60
    Rece
    34
    Frige
    33
    Frige
    31
    Arde
    Felicitari!
    Ai ghicit numarul: 31

"""

import random

random_numbers = random.randint(1,300)


number = int(input("Introduceti un numar: "))

while number != random_numbers:
    
    

    if number > random_numbers + 50 or number < random_numbers - 50:
            print("Gheata")
    elif number > random_numbers + 40 or number < random_numbers - 40:
            print("Frig")
    elif number > random_numbers + 30 or number < random_numbers - 30:
            print("Rece")
    elif number > random_numbers + 20 or number < random_numbers - 20:
            print("Caldut")
    elif number > random_numbers + 10 or number < random_numbers - 10:
            print("Cald")
    elif number > random_numbers + 5 or number < random_numbers - 5:
            print("Frige")
    elif number > random_numbers + 2 or number < random_numbers - 2:
            print("Arde")

    
    number = int(input("Introduceti un numar: "))
    
    
print("Felicitari,numarul cautat este:",random_numbers)