from auto import Car


ford = Car(4, False, False)
vw = Car(2, True, False)
toyota = Car(4, False, True)

print("START")
print(toyota.get_gas_level())

print("Alimentam 50 litri")
toyota.refill(50)

toyota.drive(0)


# vw.drive(100)

# print(vw.get_gas_level())

# vw.refill_full()

# vw.drive(200)

# print(vw.get_gas_level())

# vw.refill()

# scrieti metoda drive km pe care ii parcurge masina si return (scri doar pass)
#si consuma din curent gas volume: pt fiecare 100 de km se scade consumul
#current gas volume - 100 / 100 * cosmuation