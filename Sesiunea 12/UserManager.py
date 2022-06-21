#3. Scrie o clasa UserManger

#Atr:
# - users = lista de utilizatori activi
# - 

# Meth:
#  - add_user
#  - get_user_by_email
#  - print_user_info
#  - remove_user
#  - drop_all
#  - create_default_user


class UserManager:

    def __init__(self, users):
        self.__users = list()


    def add_user(self):
        add_user = input("Add user:")
        self.__users.append(add_user)
        print(self.__users)

    def get_user_by_email(self):
        

    def get_users(self):
        return self.__users

calatori = [
    "Otavă Bogdan",
    "Greta Mihaela Geabelea",
    "Iustin Gabriel Manciu",
    "Corina Lungu",
    "Melissa Madalina Haj Abdo",
    "Gabriel Guțui",
    "George Valeanu",
    "Andreea-Simona Telegeanu",
    "Ionuț Alin Preda",
    "Arthur Timbalariu",
    "Cristian Laurentiu Șandor",
    "Alex Raul Bonat-Mihalca",
    "Artsanyo Dennis Kachi",
    "Sergiu Mihai Predel",
    "Marian-Gabriel Tohaneanu-Iatan",
    "Irina Florentina Barbu",
    "Cordos Simona",
]




user1 = UserManager(calatori)

user2 = UserManager(calatori)


user1.add_user()

user2.add_user()

print(user2.get_users())