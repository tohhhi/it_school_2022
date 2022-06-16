"""
P1 - Phone Agenda
Utilizatorul interactioneaza cu consola, la inceput este afisat un meniu
numerotat, utilizatorul introduce un nr, urmat de Enter.

Fiecare intrare din meniu porneste un flux operational separat care atunci cand se incheie
se doreste a se revini la meniul principal.

Numele din agenda trebuie sa fie unice.

Meniu:
1. adauga contact
2. cauta contact
3. sterge contact

Fuxuri:
1. Adaugare contact
    citeste nume
    citeste nr tel
    intreaba daca doreste sa adauge alt nr.
    daca da repeta pasii
    daca nu revino la meniu principal

2. cauta contact
    introdu cateva litere > Enter
    daca stringul introdus face parte din numele din agenda
    daca sunt gasite contacte acestea sunt afisare in ordine alfabetica
    de forma:

    1. Mihai
    2. Vasile

    0: Revino la meniu

    Utilizatorul introduce un nr. corespondent numelui pe care vrea sa il vada.
    Contactul va fi afisat de forma:

    +----------------------------+
    Nume:  Xxxxxx
    Telefon: xxxx-xxx-xxx
    +----------------------------+

    0: revino la lista


3. sterge contact
    introdu numele complet
    daca acesta exista va fi sters
    daca nu o eroare este afisata.
    apoi se revine la meniu principal

"""

"""

def menu():
    print("Press 1 to add contact.")
    print("Press 2 to search contact.")
    print("Press 3 to delete contact.")

menu()

option = int(input("Enter your option:"))

while option != 0:
    if option == 1:
        name = input("Add Contact name:")
        phone_number = int(input("Add Phone number:"))
    elif option == 2:
        print("Option 2 has been called")
    elif option == 3:
        print("Option 3 has been called")
    else:
        print("Invalid option")
    
"""


option = int(input("Enter your option:"))

while option != 0:
    if option == 1: # fluxul 1
        name = input("Add name of contact:")
        number = int(input("Add phone number:"))
        user_detail = {}
        list_of_users = []
        user_detail["name"] = name
        user_detail["phone"] = number
        list_of_users.append(user_detail.copy())
        repeat = input("Do you want to add another number?").lower()
        if repeat == "yes":
            name = input("Add contact:")
            number = int(input("Add phone number:"))
            user_detail["name"] = name
            user_detail["phone"] = number
            def check_if_in_list_of_dict(sample_dict, value):
                for elem in sample_dict:
                    if value in elem.values():
                        return True
                return False
            if check_if_in_list_of_dict(list_of_users, name):
                print("Exista")
                repeat
            else:
                list_of_users.append(user_detail.copy())
                repeat
        else:
             option = int(input("Enter your option:"))
    elif option == 2: # fluxul 2 
        search = input("Search contact:") 
        if search in user_detail["name"]:
            newlist = sorted(list_of_users, key=lambda d: d["name"])
            print("+----------------------------+")
            print("Name:",user_detail["name"])
            print("Phone number:",user_detail["phone"])
            print("+----------------------------+")
        else:
            print("nu exista")
            option = int(input("Enter your option:"))
    elif option == 3: # fluxul 3
        search = input("Search contact:") 
        if search in user_detail["name"]:
            del user_detail["name"]
        else:
            print("nu exista")
            option = int(input("Enter your option:"))
    else:
        print("Invalid option")
        option = int(input("Enter your option:"))
    


