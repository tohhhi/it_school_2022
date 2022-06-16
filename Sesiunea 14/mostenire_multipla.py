class A:

    def __init__(self):
        self.count = 10

    
    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    
class B(A):
    pass

# A este supe-clasa pentru B
# B este copilul lui A / B este derivat din A

b_obj = B()

b_obj.increment()
print(b_obj.count)