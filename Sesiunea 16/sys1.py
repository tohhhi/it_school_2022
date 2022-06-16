from datetime import datetime
import sys

# oprire executie
user_choice = int(input("Enter a number:"))


if user_choice % 2 == 0:
    print("Numar par")
    print("Oprire program cu sys")
    sys.exit(1)
else:
    print("Numar impar")
    print("Programul va continua")


print(datetime.now())