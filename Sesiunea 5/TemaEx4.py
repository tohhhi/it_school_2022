#4. Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
#un singur agument reprezentand muchia cubului in metri.


def volume_to_liters(value):
    return value ** 3 * 1000


print(volume_to_liters(30))