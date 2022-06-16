#7. Scrieti un program care citeste doua nr de la tastatura si calculeaza produsul
#lor. A nu se utiliza operatorul de inmultire. 
# 3×4=3+3+3+3=12

def produs(a, b):
    """Product of two numbers."""
    res = 0
    for i in range(b):
        res = res + a 
    return res

print(produs(4, 4))
# print(12)

x_result = produs(30, 23)

# x * n = x + x + x + x .... de n ori

    
    


    
        

    
