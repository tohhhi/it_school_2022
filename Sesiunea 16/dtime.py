# Ora si data curenta?

from datetime import datetime

current_dt = datetime.now()   # metoda statica

# Ziua curenta
print("Ziua:",current_dt.day)

# Luna curenta
print("Luna:",current_dt.month)

# anul curent
print("Anul:",current_dt.year)

# ora curenta
print("Ora:",current_dt.hour)

# minute si secunde
print("Minut:",current_dt.minute)
print("Secunda:",current_dt.second)

