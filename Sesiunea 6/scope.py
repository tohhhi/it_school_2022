# global scope
rev = 20
PI = 3.14
age = 20

def bar():
    #local scope 
    age = 1
    age1 = age + 10
    print(age1)


def p_cerc(r):
    return 2 * PI * r





bar()

def reverse(n):
    rev = 0 
    while n != 0:
        c = n % 10 # rest
        n = n // 10 # cat
        rev = rev * 10 + c

    return rev



rev = 100