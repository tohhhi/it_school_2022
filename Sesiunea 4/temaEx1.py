#1. Scrieti un program care afiseaza numerele prime din intervalul [0 100].

for n in range(0, 100):
    prim = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    if prim:
        print(n)
        