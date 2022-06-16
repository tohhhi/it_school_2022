# 1) Write a function to set None at a specified key in a dict


user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}



def set_none(val):
    for i in user_info.keys():
        user_info[val] = "None"
        

set_none("age")

set_none("gender")

print(user_info)



        


        

