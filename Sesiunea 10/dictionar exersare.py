# 1. Accesare si printare dictionar.
# 2. Adaugam o noua valoare in dictionar.
# 3. Adaugare key si value (cheie si valoare) in dictionar.
# 4. Stergere date dintr-un dictionar.
# 5. Cum extragem lista cheilor
# 6. lista keylor
# 7. lista valorilor
# 8. Lista cheilor si valorilor 
# 9. Tuple unpaking




# 1
user_info = {
    "name": "Vasile",
    "age": 19,
    "nationality": "Romanian",
    "gender": "Male"
}

print(user_info.get("name"))

print(user_info["gender"])

print(user_info.get("age"))

# 2

user_info["name"] = "Marian"

print(user_info)



# 3
 

user_info["car license"] = "yes"

print(user_info)

# 4

del user_info["car license"]

print(user_info)

print("--------------")

# 5 

print(user_info.keys())


print("--------------")

#6

user_info = {
    "name": "Vasile",
    "age": 19,
    "nationality": "Romanian",
    "gender": "Male"
}

k_user_info = user_info.keys()

for k in user_info.keys():
    print(k)


print(len(user_info))


user_info["adrress"] = "Str.George Murnu"


if k_user_info == 4:
    print("Dictionar neschimbat")
else:
    print("Dictionar updatat")

print(type(k_user_info))


# 7

user_info = {
    "name": "Vasile",
    "age": 19,
    "nationality": "Romanian",
    "gender": "Male"
}

v_user_info = user_info

for v in v_user_info.values():
    print(v)

print("--------------")

# 8

user_info = {
    "name": "Vasile",
    "age": 19,
    "nationality": "Romanian",
    "gender": "Male"
}

k_v = user_info




# 9

user_info = {
    "name": "Vasile",
    "age": 19,
    "nationality": "Romanian",
    "gender": "Male"
}

for k,v in user_info.items():
    print("Detaliile participantului",k,"numele si datelel lui",v)