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

n = None
x = random.randint(1,300)






while n != x:

    n = int(input("Introduceti un numar: "))
    
    
    


print("Felicitari, numarul cautat este:", x)