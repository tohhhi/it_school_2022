


def menu():
    print("Pentru adaugare contact tastati 1.")  
    print("Pentru cautare contact tastati 2.") 
    print("Pentru a sterge contact tastati 3.")

    option_menu = int(input("Alege:"))

    while True:
        if option_menu == 1:
            add_contact
        elif option_menu == 2:
            print("Execute option 2")
        elif option_menu == 3:
            print("Execute option 3")
        elif option_menu == 0:
            menu


menu()



def add_contact():

    name = input("Adaugare nume contact:")
    number = int(input("Adaugare numar de telefon:"))
    id = 0
    list_of_users = []
    user_detail = {}

    user_detail = {
        "name":name,
        "phone_number":number,
     "id": id
    }
    list_of_users = []
    list_of_users.append(user_detail)

    print(list_of_users)


add_contact
