"""
8. Scrieti un program de tip joc "ghiceste numarul".
    Cerinte: 
    1. Programul genereaza un numar aleator in intervalul [1, 99].
    2. Intr-o bucla conditionata de gasirea numarului cautat:
        - se citeste de la tastatura un numar
        - se compara cu numarul cautat
        - daca numarul introdus este mai mic decat numarul cautat se afiseaza +
        - daca este mai mic se afiseaza -
    3. Dupa ce numarul este ghicit se afiseaza un mesaj de felicitare si numarul cautat.
"""

import random

random_numbers = random.randint(1,100)


number = int(input("Introduceti un numar: "))

while number != random_numbers:
    if number > random_numbers:
            print("-")
    elif number < random_numbers:
            print("+")
    number = int(input("Introduceti un numar: "))
print("Felicitari,numarul cautat este:",random_numbers)
  
     

    
    
    
    
    