"""
user_name = set()

n = 0

while n < 4:
    name = input()
    user_name.add(name)
    n += 1


print(user_name)

"""

user_name = set()

user_name.add("Mihai")
user_name.add("Alex")
user_name.add("George")
print(user_name)

if "Mihai" in user_name:

    user_name.remove("Mihai")

print(user_name)


user_name.clear()

print(user_name)