def produs(a, b):
    """Product of two numbers."""
    res = 0
    for i in range(b):
        res += a
    return res
    


print(produs(3, 4))
# print(12)


x_result = produs(30, 23)

print(x_result + 2)