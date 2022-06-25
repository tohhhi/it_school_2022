from datetime import datetime
from math import pi



def circle_area(radius):
    """Calculeaza aria cercului, doar pentru numere pozitive.

    Args:
        * radius int or float: Raza cercului.

    Returns:
        float: Aria cercului

    Raises:
        * ValueError: Daca radius este numar negativ.
        * TypeError: Daca radius nu este numar.
    """
    if isinstance(radius, float) or isinstance(radius, int):
        if radius < 0:
            raise ValueError("Nu pot calcula aria pentru un numar negativ.")
        return pi * radius ** 2
    else:
        raise TypeError("Nu pot calcula aria pentru parametru introdus.") # se creeaza un obiect nou de tip expectie

def cylinder_volume(radius, height):
    return circle_area(radius) * height

# height = int(input("Inaltime: "))
# radius = int(input("Raza: "))
# print(f"Volum cilindru: {cylinder_volume(radius, height)}")

try:
    print(circle_area("Str"))
except (ValueError, TypeError) as err:
    print(f"{datetime.now()} [ERROR] {err}")


print(circle_area(2.3))