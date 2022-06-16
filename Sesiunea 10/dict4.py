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

colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF"
}



# lista chei-valori

k_v_china_years = china_years.items()

print(k_v_china_years)

#[
#
#(2010, 'Dragonului'), 
#(2011, 'Cocosului'), 
#(2012, 'Iepurelui')

#]

for kv in china_years.items():
    print("Anul", kv[0], "a fost anul", kv[1])


for k, v in china_years.items():
    # k, v = (2010, 'Dragonului)
    print("Anul", k, "a fost anul", v)