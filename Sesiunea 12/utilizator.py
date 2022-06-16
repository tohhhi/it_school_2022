"""
2. Scrie o clasa care repr. un Utilizator
Atr:
 - nume
 - prenume
 - telefon
 - email
 - activ - bool

Meth: 
 - activate
 - deactivate
 - update_email - 1 param
 - update_phone - 1 param

"""

class Utilizator:

    def __init__(self):
        self.__nume = "Tohaneanu"
        self.__prenume = "Marian"
        self.__telefon = "0755621608"
        self.__email = "tohaneanu.marian@yahoo.com"
        self.__activ = bool


    def activate(self):
        print("Utilizator activat.")
        return self.__activ == True 
        

    def deactivate(self):
        print("Utilizator dezactivat.")
        return self.__activ == False

    def update_email(self, email):
        self.__email = email
        return self.__email

    def update_phone(self, phone):
        self.__telefon = phone
        return self.__telefon
        


user1 = Utilizator()
user2 = Utilizator()
user3 = Utilizator()



print(user1.update_phone("0744395074"))

print(user1.update_email("marian_andrei@gmail.com"))

user1.activate()

user1.deactivate()







