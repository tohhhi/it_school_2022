for i in range(1, 101):
    if i % 2 == 1:
        print(i)



n = 14

for i in range(2, 13):
    if n % i == 0:
        print("Numarul nu este prim!")


#3. Scrieti un program care citeste de la tastatura un nr natural "n", 
#si afiseaza suma primelor n numere multiple de 5 si 3.

n = input("Introduceti un numar: ")
n = int(n)

suma = 0

for i in range(3, n, 3):
    if i % 5 == 0:
        suma = suma + i
print(suma)


