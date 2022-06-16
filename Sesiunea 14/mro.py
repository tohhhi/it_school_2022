class A:

    def say_test(self):
        print("Hello from A")

class B(A):

    def say_test(self):
        print("Hello form B")



class C(B):

    def say_test(self):
        print("Hello from C")



c = C()

c.say_test()

# MRO - method resolution order
# este folosit pt mostenire sa vedem care metoda sa o execute


print(C.mro())