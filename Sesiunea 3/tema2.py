# 2. Scrie un program care citeste de la tastatura un numar 
# natural, reprezentand raza unui cerc, si afiseaza perimetrul
# cercului insotit de mesajul "Perimetru cercului = <valoare>".
# Daca numarul citit este mai mare decat 100 se va calcula si aria
# cercului. Aceasta se va afisa insotita de mesajul "Aria cercului = <valoare>".

from turtle import done


raza_cercului = input("Introdu un numar: ")

raza_cercului = int(raza_cercului)

perimetru_cerc = 2 * 3.14 * raza_cercului

perimetru_cerc = int(perimetru_cerc)

print("Perimetru cercului:" , perimetru_cerc)

aria_cercului = 3.14 * raza_cercului ** 2

if raza_cercului > 100:
    print("Aria cercului este: " , aria_cercului)
else:
    done
