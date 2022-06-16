from lib2to3.pgen2 import driver


class Car:

    # constructor
    def __init__(self, doors, automatic, awd):  # dunderscore methods | magic methods
        # print("---Constructor apelat---")
        # definire atribute
        # self.xxxxxxx = yyyyyyy

        # modificator de access
        # _xxxx -> protected
        # __xxxxxx -> private


        # private
        # public attribute
        self.__km = 0
        self.__doors = doors
        self.__automatic = automatic  # sau manual
        self.__awd = awd  # AWD = all wheel drive = 4x4
        
        self.__gas_tank_volume = 70
        self.__current_gas_volume = 0

        self.__wipers = False

        self.__consumption = self.__calculate_consumption()

    # definire metode
    
    def drive(self,km):
        return self.__current_gas_volume - 100 / 100 * self.__calculate_consumption
    
    
    
    def horn(self):
        print("titititiii")

    def describe(self):
        print("Doors:", self.__doors)
        print("Transmission:", self.__automatic)
        print("AWD:", self.__awd)
    
    def get_km(self):
        return self.__km

    
    def get_gas_level(self):
        return self.__current_gas_volume / self.__gas_tank_volume  * 100

    def refill(self, gas_liters):
        if 0 <= gas_liters <= self.__gas_tank_volume - self.__current_gas_volume:
            self.__current_gas_volume += gas_liters

    def refill_full(self):
        self.__current_gas_volume = self.__gas_tank_volume

    def turn_on_wipers(self):
        self.__wipers = True

    def turn_off_wipers(self):
        self.__wipers = False

    # metoda privata
    def __calculate_consumption(self):
        points = 0
        if self.__doors > 2:
            points += 3
        else:
            points += 2
        
        if self.__automatic:
            points += 3
        else:
            points += 2
        
        if self.__awd:
            points += 3
        else:
            points += 2

        return points

    def __del__(self):
        # destructor
        pass
        # print("Obiect sters")