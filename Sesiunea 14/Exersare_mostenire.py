# 1. Scrieti o clasa Shape care are o metoda arie (nu are nimic scriem cu pass)
# 2. Scrieti o clasa Circle care mosteneste shape si suprascrie metoda arie 
# 3. Scrieti o clasa Square care mosteneste shape si si suprascrie metoda arie .



class Shape:
    
    def arie(self):
        pass


class Circle(Shape):

    def arie(self, r):
        return 3.14 * r ** 2


class Square(Shape):

    def arie(self, l):
        return l ** 2



circle = Circle()

square = Square()

print(circle.arie(14))

print(square.arie(12))
        

        
        
    
    

