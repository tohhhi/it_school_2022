# 4) Make list of dictionaries, each dictionaries contains the following attributes: name, age, gender; Read those info from keyboard input.
# 5) sort list by users age




user_info = {}
list_of_users = []


u = int(input("Cati utilizator vreti sa adaugati:"))
i = 0

while i < u:
    i = i+ 1
    name = input("Introduceti un nume:")
    age = int(input("Introduceti varsta:"))
    gender = input("Introduceti genul:")

    
    
    user_info["name"] = name
    user_info["age"] = age
    user_info["gender"] = gender

    list_of_users.append(user_info.copy())
    
    newlist = sorted(list_of_users, key=lambda d: d['age']) 
   
    

    

        
print(list_of_users)
    
    
     





# mai intai fac un dictionar dp il salvez in lista