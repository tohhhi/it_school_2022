user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}


# lista cheilor

u_i_keys1 = list(user_info.keys())
for key in u_i_keys1:
    print(key)

user_info["address"] = "Bucharest"

print("-" * 30)
for key in u_i_keys1:
    print(key)


if len(u_i_keys1) == len(user_info.keys()):
    print("Dictionar nemodificat")
else:
    print("Dictionar modificat")


