user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

china_years = {
    2010: "Dragonului",
    2011: "Cocosului",
    2012: "Iepurelui"
}

# sortare dupa chei
sorted_user_info = sorted(user_info.items())

print("Sortat dupa chei")
for k, v in sorted_user_info:
    print(k, "||", v)


# sortat dupa valori
print("Sortat dupa valori")

def comparator(t):
    return t[1]


for k, v in sorted(china_years.items(), key=comparator):
    print("Anul", k, "a fost anul", v)


# sau cu lambda

for k, v in sorted(china_years.items(), key=lambda x: x[1]):
    print("Anul", k, "a fost anul", v)


