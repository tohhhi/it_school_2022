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

    def __init__(self):
        self.__users = []


    def add_user(self, email_user):
        self.__users.append(email_user)
        
    def delete_user(self, delete_user):
        self.__users.remove(delete_user)
    
    def drop_all(self):
        self.__users.clear()
    

    def get_users(self):
        return self.__users



user1 = UserManager()


user1.add_user("madalin.01@gmail.com")

user1.add_user("andrei_steaua98")

user1.add_user("tohaneanu.marian@yahoo.com")


print(user1.get_users())

user1.delete_user("andrei_steaua98")

print(user1.get_users())

user1.drop_all()

print(user1.get_users())

user1.add_user("tohaneanu.marian@yahoo.com")

print(user1.get_users())


