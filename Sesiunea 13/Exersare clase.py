class AirTrip:

    def __init__(self, depart_airport, arrive_airport, price):
        self.__depart_airport = depart_airport
        self.__arrive_airport = arrive_airport
        self.__price = price


    def get_price_tva(self):
        return self.__price * 1.19 




bilet = AirTrip("Manile", "otopeni", 120)

print(bilet.get_price_tva())