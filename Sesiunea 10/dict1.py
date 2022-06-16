empty_dict = {}
empty_dict1 = dict()

user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

#user_info1 = ["Alex", 28, "alex.radu@email.com", "M"]

#accesare
print("Nume:", user_info["name"])
print("Varsta:", user_info["age"])

print(user_info.get("name", "Negasit"))

#modificare
print("-------------------------")

user_info["name"] = "George"

print("Nume:", user_info["name"])
print("Varsta:", user_info["age"])


# adaugare

print(empty_dict)

empty_dict["ro"] = "Buna ziua!"

print(empty_dict)

empty_dict["en"] = "Good afternoon!"

print(empty_dict["en"])

# stergere
print("----------------------")
del user_info["email"]

print(user_info)

# CRUD - create read update delete
empty_dict1 = {
    2010: "Dragon",
    2011: "Cocos",
    2012: "Iepure"
}

empty_dict1[2013] = "Catel"

print(empty_dict1[2013])


fool = {
    2: "Two",
    2.0: "Also two",
    2.1: "Almost two"
}

print(fool[2])