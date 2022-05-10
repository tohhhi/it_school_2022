#4. Scrieti un program care citeste de la tastatura un nr natural "n", 
#si afiseaza n! (factorial). 6! = 1 * 2 * 3 * 4 * 5 * 6

n = input("Introduceti un numar: ")

n = int(n)

for i in range(n, 2, n):
    if 