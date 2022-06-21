from datetime import datetime

# 4. Print your birth date formatted as MM/dd/YYYY

my_birthday = datetime(1998,9,8)

print(my_birthday.strftime("%m/%d/%Y"))