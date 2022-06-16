# Principiile Programarii Orientate pe Obiect:

# 1. Abstractizarea

# 2. Incapsularea

# 3. Polimorfismul 

# 4. Mostenirea


# Definire clasa:




class Car:  # -> Car este o clasa
    pass


print(Car)


# instantiere

automobil = Car() # -> automobil este un obiect

print(automobil)


# definire metode intr o clasa

class Car:




    # definire metode
    def horn(self):
        print("TITIT")

    
    def get_gas(self):
        return 100



BMW = Car()

BMW.horn()
print(BMW.get_gas())



# Structura OOP:

# 1. Definire Clasa
# 2. Constructor
# 3. Metode
# 4. Instantiere - Creeare obiect



class Moto:  # --> definire clasa

    def __init__(self): # --> Constructor (metoda magica)
        print("---Constructor apelat---")
        # definire atribute
        self.__top_speed = 299
        self.__gas_per = 100


 
    # Definire metode
    def max_speed(self):  # --> Metoda
        return self.__top_speed

    def gears(self): # --> Metoda
        return 6

    def get_gas(self):
        return self.__gas_per

    def refill_gas(self, g_p):
        if g_p > self.__gas_per:
            self.__gas_per = g_p
        else:
            self.__gas_per =+ g_p


Ducati = Moto()  # --> Creare Obiect

Honda = Moto()

print(Ducati.max_speed())

print("Viteza maxima motocicleta:",Ducati.max_speed(),"km/h")

print("Motocicleta are:",Ducati.gears(),"viteze.")

print("Rezevorul motocicletei este:",Honda.get_gas(),"%")

Honda.refill_gas(25)

print("Rezevorul motocicletei este:",Honda.get_gas(),"%")