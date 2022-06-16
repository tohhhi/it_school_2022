class Plane:

    def __init__(self, engines, doors):
        print("Creating new plane")
        self.engines = engines
        self.doors = doors
        self.length = 50
        self.wing_span = 33
        self.tank_volume = 22
        self.__engine_on = False

    def start_engine(self):
        print("Starting engine...")
        self.__engine_on = True

    def is_engine_running(self):
        return self.__engine_on


class CargoPlane(Plane):
    
    def start_engine(self):
        print("Start big engine...")
        print("Start big engine...")
        # super() ne da acces la medodele clasei parinte
        return super().start_engine()
    
    def open_cargo_doors(self):
        pass


class Airliner(Plane):
    
    def __init__(self):
        super().__init__(2, 8)
        self.seat_number = 100


class PrivatePlane(Plane):
    pass

class Glider:
    pass

cargo_p = CargoPlane(4, 8)
airliner = Airliner()
private_p = PrivatePlane(1, 2)



# print(cargo_p)
# print(airliner)
# print(private_p)


# cargo_p.start_engine()
# print(cargo_p.is_engine_running())

# airliner.start_engine()
# print(airliner.seat_number)
# print(airliner.is_engine_running())

# print(private_p.is_engine_running())
# DRY - do not repeat yourself

def prepare_for_takeoff(plane):
    """Configureaza avionul pentru decolare."""

    print("Configure plane for takeoff...")
    if isinstance(plane, Plane):
        plane.start_engine()
    print("Taking off....")

# print(isinstance(cargo_p, CargoPlane))
# print(isinstance(cargo_p, Plane))
# print(isinstance(cargo_p, object))


# print(type(type))

# prepare_for_takeoff(glider)
# prepare_for_takeoff(cargo_p)


