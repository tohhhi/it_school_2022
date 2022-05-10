def is_even(n):
    """"Check if the number is even."""
    if n % 2 == 0:
        return True
    else:
        return False



for i in range(10):
    if is_even(i):
        print(i, "este par")
    else:
        print(i, "este impar")