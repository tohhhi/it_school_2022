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


# 1. Adaugare contact
#    citeste nume
#    citeste nr tel
#    intreaba daca doreste sa adauge alt nr.
#    daca da repeta pasii
#    daca nu revino la meniu principal


name = input("Adaugare nume contact:")
number = int(input("Adaugare numar de telefon:"))
id = 0
list_of_users = []
user_detail = {}

def add_contact():

    user_detail = {
        "name":name,
        "phone_number":number,
     "id": id
    }
    list_of_users = []
    list_of_users.append(user_detail)

    print(list_of_users)

# 2. Cautare contact
# 2. cauta contact
#    introdu cateva litere > Enter
#    daca stringul introdus face parte din numele din agenda
#    daca sunt gasite contacte acestea sunt afisare in ordine alfabetica
#    de forma:
#
#    1. Mihai
#    2. Vasile

#    0: Revino la meniu

#    Utilizatorul introduce un nr. corespondent numelui pe care vrea sa il vada.
#    Contactul va fi afisat de forma:

#    +----------------------------+
#    Nume:  Xxxxxx
#    Telefon: xxxx-xxx-xxx
#    +----------------------------+

#    0: revino la lista

def search_contact():

    search_contact = input("Cauta un nume:")


    if search_contact in user_detail["name"]:
        list_of_users.sort()
        print(id, user_detail["name"])
    else:
        print("Acest nume nu exista.")


# Stergere contact:
#3. sterge contact
#    introdu numele complet
#    daca acesta exista va fi sters
#    daca nu o eroare este afisata.
#    apoi se revine la meniu principal

def delete_contact():

    delete_contact = input("Introduceti numele care vreti sa il stergeti:")

    if delete_contact in user_detail["name"]:
        user_detail.pop("name")
    else:
        print("Acest nume nu exista.")

    print(list_of_users)