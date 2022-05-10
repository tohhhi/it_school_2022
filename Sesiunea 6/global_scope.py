# global scope
PI = 3.1

# de evitat
def correct_pi():
    global PI
    PI = 3.14154142



def p_cerc(r):
    #local scope
    return 2 * PI * r

correct_pi()

print(p_cerc(10))