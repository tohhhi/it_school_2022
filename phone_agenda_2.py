id = 1
list_of_users = []


def menu():
    print("-----------------Menu-----------------")
    print("| Pentru adaugare contact tastati 1  |")  
    print("| Pentru cautare contact tastati 2   |") 
    print("| Pentru a sterge contact tastati 3  |")
    print("| Pentru a reveni la meniu tastati 0 |")
    

    option_menu = int(input("Alege:"))

    while True:
        if option_menu == 1:
            add_contact()
            add_another_contact()
            menu()
            break
        elif option_menu == 2:
            search_contact()
            see_all_contacts()
            contact_full_info()
            return_to_menu()
            break
        elif option_menu == 3:
            delete_contact()
            menu()
            break
        elif option_menu == 0 or return_to_menu() == 0:
            menu()
            break






def add_contact():
    global id

    name = input("Adaugare nume contact:")
    number = int(input("Adaugare numar de telefon:"))
    

    list_of_users.append(
        {
         
            "name":name,
            "phone_number":number,
            "id": id
        }
    )
    
    
    id += 1
    print(list_of_users)
    

def add_another_contact():
    add_another_contact = input("Doriti sa adaugati alt numar? yes/no:").lower()
    if add_another_contact == "yes":
        add_contact()
    elif add_another_contact == "no":
        menu()

def search_contact():

    search_contact = input("Cauta un nume:")
    
    for i in list_of_users:
        if search_contact in i["name"]:
            print(i["id"],i["name"])
            break
        elif search_contact not in i["name"]:
            print("Contactul cautat nu exista.")
            break
       
    
        
   
            

  
def see_all_contacts():
    see_all_contacts = input("Doriti sa vedeti toate contactele din agenda? yes/no:").lower()
    if see_all_contacts == "yes":
        for i in list_of_users:
            print(i["id"],i["name"])
    elif see_all_contacts == "no":
        menu()


def delete_contact():

    delete_contact = input("Introduceti numele care vreti sa il stergeti:")

    for i in range(len(list_of_users)):
        if list_of_users[i]["name"] == delete_contact:
            del list_of_users[i]
            break
        
    if list_of_users[i]["name"] != delete_contact:
            print("Acest nume nu exista in agenda.")

    print(list_of_users)

def contact_full_info():
    info = int(input("contact full info:"))
    
    for i in range(len(list_of_users)):
        if info == list_of_users[i]["id"]:
            print("+----------------------------+")
            print("Nume: " , list_of_users[i]["name"])
            print("Telefon:", list_of_users[i]["phone_number"])
            print("+----------------------------+")



def return_to_menu():
    return_to_menu = int(input("Pentru a reveni la meniu apasati 0:")) 
    if return_to_menu == 0:
        menu()
    

    


menu()