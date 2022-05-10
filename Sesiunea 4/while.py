"""

while conditie:
    cod - instructiuni
    cod
    cod
"""


# executam de 3 x print
from re import X


n = 0



while n < 3:
    print("Hello")
    n = n + 1


# 1. n = 0
# 2. n = 1
# 3. n = 2
# 4. n = 3 - nu se executa


n = 6
k = 1

n = int(input("Introdu n: "))
k = 1


while k <= n:
    print("*" * k, "+" * (n - k), sep="" )
    k = k + 1
print("DONE")   
    

# *++ k - stelute; n - k plusuri
# **+
# ***