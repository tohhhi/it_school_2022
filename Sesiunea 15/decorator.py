import time
from datetime import datetime


# debug decorator


def cube_volume(edge):
    """Calculate cube volume in liters. """
    # 1 m3 = 1000 de litri
    return edge ** 3 * 1000

l = 29

print("S-a apelat functia cube_volume la ora", datetime.now(),"pentru edge =",l)
start = time.time()
cube_volume(l)
stop = time.time()
print("Apelul a durat x secunde", stop - start)


# decoratorul trebuie sa returneze o alta functie 
def debuger():
    def inner():
        f()

    return inner



    