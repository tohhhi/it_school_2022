class Car:

    def __init__(self, doors, automatic, awd):
        self.__km = 0
        self.__doors = doors
        self.__automatic = automatic
        self.__awd = awd
        self.__wipers = False
        self.__gas_tank_volume = 70
        self.__current_gas_volume = 0
        self.__consumption = self.__calculate_consumption()


    def horn(self):
        print("TITITI")

    def get_km(self):
        return self.__km
    
    def drive(self, km):
        self.__km = km 
        self.__current_gas_volume = self.__current_gas_volume - km / 100 * self.__consumption


    def description(self):
        print("Doors:",self.__doors,"Transmission:",self.__automatic,"AWD:",self.__awd)

    def get_gas_level(self):
        return self.__current_gas_volume / self.__gas_tank_volume * 100


    def refill(self, liters):
        if 0 <= liters <= self.__gas_tank_volume - self.__current_gas_volume:
            self.__current_gas_volume += liters

    def refill_full(self):
        self.__current_gas_volume = self.__gas_tank_volume
        
    def turn_on_wipers(self):
        self.__wipers = True

    def turn_off_wipers(self):
        self.__wipers = False


    def __calculate_consumption(self):
        points = 0
        if self.__doors >= 2:
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


volvo = Car(4, True, True)
vw = Car(2, True, False)

ford = Car(4, False, False)


print(volvo.get_gas_level())

volvo.refill_full()

print(volvo.get_gas_level())

volvo.drive(350)

print(volvo.get_gas_level())

volvo.refill(20)

print(volvo.get_gas_level())

print(volvo.get_km())