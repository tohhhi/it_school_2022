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

    def __init__(self, nume, prenume, telefon, email, activ):
        self.__nume = nume
        self.__prenume = prenume
        self.__telefon = telefon
        self.__email = email
        self.__activ = activ


    def activate(self):
        print("Utilizator activat.")
        self.__activ = True
        return self.__activ  
        

    def deactivate(self):
        print("Utilizator dezactivat.")
        self.__activ = False
        return self.__activ 

    def update_email(self, email):
        self.__email = email
        return self.__email

    def update_phone(self, phone):
        self.__telefon = phone
        return self.__telefon

    def view_detail_of_users(self):
        print(self.__nume, self.__prenume, self.__telefon, self.__email, self.__activ)     


user1 = Utilizator("Tohaneanu", "Marian", "0755621608", "tohaneanu.marian@yahoo.com", True)
user2 = Utilizator("Stroe", "Andrei", "0744395074", "stroe.andrei@gmail.com", True)
user3 = Utilizator("Anisiei", "Marius", "0754123554", "anisiei.marius@yahoo.com", False)


user1.update_email("marius")

user1.update_phone("213041941")

user1.view_detail_of_users()

user1.deactivate()

user1.view_detail_of_users()

user2.view_detail_of_users()

user2.deactivate()

user2.view_detail_of_users()

user2.update_email("stroe_andrei@yahoo.com")

user2.view_detail_of_users()

user2.activate()

user2.view_detail_of_users()










