#4. Scrieti un program care citeste de la tastatura un nr natural "n", 
#si afiseaza n! (factorial). 6! = 1 * 2 * 3 * 4 * 5 * 6



def factorial(n):
    
    if n == 1:
        return 1
    return factorial(n - 1) * n
    



print(factorial(10))