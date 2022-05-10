for i in range(10):
    print(i)


# range(10) produce intervalul [0, 10) - nu il introduce pe 10;

# range(3) -> 0 1 2

# 1. i = 0
# 2. i = 1
# 3. i = 2


for i in range(1, 3):
    print("Iteratia: " , i + 1)
    print("i =", i)


# range(10) -> [0,10) -> 0 ... 9
#range(stop)

# range (3, 10) -> [3,10) -> 3 ... 9
#range(start, stop)

#range(3, 10 ,2) -> 3, 5, 7, 9
#range(start, stop, pas)

#range (11 , 0 ) -> nu afiseaza nimic

#range (10 , -1 , -1) -> 10, 9 ,8 ... 0 
