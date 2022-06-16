

option = int(input("Enter your option:"))

while option != 0:
    if option == 1:
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
    elif option == 2:
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
    elif option == 3:
        search = input("Search contact:") 
        if search in user_detail["name"]:
            del user_detail["name"]
        else:
            print("nu exista")
            option = int(input("Enter your option:"))
    else:
        print("Invalid option")
        option = int(input("Enter your option:"))
    
    