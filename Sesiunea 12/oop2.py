from auto import Car

volvo = Car() # aici se apeleaza constructorul automat
vw = Car()

# accesare atribute
print("Volvo gas:", volvo.get_gas())
print("VW gas:", vw.get_gas())

volvo.refill_full()
vw.refill(20)
print("----------------------------------------")

print("Volvo gas:", volvo.get_gas())
print("VW gas:", vw.get_gas())

