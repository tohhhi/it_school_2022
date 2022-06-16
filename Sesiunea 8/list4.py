from sys import last_traceback


user_id = [33, 455, 3, 32, 34, 12, 90, 3, 234]

# reversul listei !! opereaza pe lista
print("Lista in stare initiala")
print(user_id)


user_id.reverse()

print("Dupa reverse")
print(user_id)

# list sliceing
# primele 3 elemente
top_three_users = user_id[:3]

print("user_id", user_id)
print("top_three_users", top_three_users)


# ultimul element
last_element = user_id[-1:]
print(last_element)


print(user_id[1:4])