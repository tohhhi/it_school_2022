#2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
#[0, 50] si in intervalul [2000, 2100].

def functie(number):
    if number % 2 == 0:
        return True
    else:
        return False


for i in range(0,51):
    print(functie(i))


for i in range(2000, 2101):
    print(functie(i))