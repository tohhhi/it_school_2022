
# continue
# break


# continue = omite iteratia curenta
# break = opreste iteratia


# 15 % 3 => 0
# 30 % 3 => 0

#15; 30
for i in range(2, 15):
    if 15 % i == 0 and 30 % i == 0:
        print(i)
        break


for i in range(10):
    if i % 2 == 1:
        print("Ceva")
    print(i)
