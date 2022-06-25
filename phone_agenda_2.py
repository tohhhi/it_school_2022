id = 0
list_of_users = []
user_detail = {}



def menu():
    print("Pentru adaugare contact tastati 1.")  
    print("Pentru cautare contact tastati 2.") 
    print("Pentru a sterge contact tastati 3.")
    print("Pentru a reveni la meniu tastati 0.")

    option_menu = int(input("Alege:"))

    while True:
        if option_menu == 1:
            add_contact()
            break
        elif option_menu == 2:
            print("execute")
            search_contact()
            break
        elif option_menu == 3:
            print("Execute option 3")
            break
        elif option_menu == 0:
            menu()
            break






def add_contact():

    name = input("Adaugare nume contact:")
    number = int(input("Adaugare numar de telefon:"))
    id = 0
    global list_of_users
    global user_detail

    user_detail = {
        "name":name,
        "phone_number":number,
        "id": id
    }
    list_of_users = []
    list_of_users.append(user_detail)

    print(list_of_users)
    menu()
    return list_of_users, user_detail, id

    

def search_contact():

    search_contact = input("Cauta un nume:")
    


    if search_contact in user_detail["name"]:
        list_of_users.sort()
        print(id, user_detail["name"])
    else:
        print("Acest nume nu exista.")




menu()