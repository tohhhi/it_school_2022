import time


# help si dir 

now = time.time()

print(now)

print(time.time())


start = time.time()

for i in range(10000):
    print(10 ** i)


stop = time.time()


print("Started at", start)
print("End at:", stop)
print("Duration", stop - start)