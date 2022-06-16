#7.Scrie un program care citeste de la tastatura un nr.natural 
# si verifica daca acesta este palindrom. 111 121 292 2992 33533

# Functie care returneaza True daca un nr este palindrom.

# Citim de la tastatura un nr

# Apelam fct.

# 178 == 871 False
# 121 == 121 True


# 178
# 8
# 17
# 7
# 1
#

# PENTRU INTERVIU.

# 871
# 87
# 8
# 0 








def reverse(n):
    rev = 0 
    while n != 0:
        c = n % 10 # rest
        n = n // 10 # cat
        rev = rev * 10 + c

    return rev

def palindrom(n):
    """Check if palindrom"""
    if n == reverse(n):
        return True
    else:
        return False

n = int(input("Introduceti un numar: " ))

if palindrom(n):
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")









