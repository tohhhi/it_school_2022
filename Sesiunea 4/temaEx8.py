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

number = input("Introduceti un numar: ")
number = int(number)

lucky_number = 55

for n in range(1,101):
    if number < lucky_number:
        print("+")
    else:
        print("-")
    if number == lucky_number:
        print("Felicitari!")
    
    