#5. Scrieti o functie care returneaza volumul unui cilintru in litri,
#Aceasta va primi doua argumente reprezentand inaltimea si raza bazei in metri.

def cilinder_in_liters(h,r):
    return 3.14 * r ** 2 * h


print(cilinder_in_liters(10,5))