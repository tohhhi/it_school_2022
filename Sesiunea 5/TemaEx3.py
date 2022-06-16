#3. Scrieti o functie care returneaza daca unu nr. (reprezentan un an) este
#considerat an bisect.


def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


print(leap_year(2013))

print(leap_year(2016))

print(leap_year(2024))