# global scope
index = 10 


for index in range(100, 20, -10):
    # local scope
    print(index)


# for loop variable leaking
print(index)


# while 

n = 2

while n != 0:
    index = 1
    print(n)
    n -= 1

print(index)