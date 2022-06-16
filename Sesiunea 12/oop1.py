# definire clasa
# naming rules:
# NumeleDeClasa - CapsCase


from msilib import type_key


class Car:   # Car -> este o clasa
    pass


class AirplaneTicket:
    pass



#print(Car)
#print(type(Car))

# instantiere
# automobil -> este un obiect

automobil = Car()

#print(automobil)
#print(type(automobil))

# verificare ca un obiect face parte dintr-o clasa
print("automobil este Car")
print(isinstance(automobil,Car))
