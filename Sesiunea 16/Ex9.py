from datetime import datetime

#9. wite a script that calculates first 1000 numbers from Fibonacci sequence and 
#print how much execution took.

startTime = datetime.now()

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()


fib(1000)

print(f"Executia a durat:{datetime.now() - startTime}.")