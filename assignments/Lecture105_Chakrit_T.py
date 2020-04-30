class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAir(self):
        print("Turn On : Air")
class car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass
car1 = car()
print("car1")
car1.turnOnAir()
PickUp1 = PickUp()
print("PickUp1")
PickUp1.turnOnAir()
Van1 = Van()
print("Van1")
Van1.turnOnAir()
EstateCar1 = EstateCar()
print("EstateCar1")
EstateCar1.turnOnAir()