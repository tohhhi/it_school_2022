# 5) Extract the number from import_numbers variable.

import_numbers = "Today we had 280 clients."

# metoda 1
number_of_clients = import_numbers[-12:-9]

print(number_of_clients)

# metoda 2 
number = import_numbers.split()[3]

print(number)

