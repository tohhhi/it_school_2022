from random import randint


class Card:

    # atribut static
    counter = 0

    def __init__(self, number, symbol):
        Card.counter += 1
        self.number = number
        self.symbol = symbol

    def __str__(self):
        return self.number + self.symbol

    def __repr__(self):
        return self.__str__()


for i in range(randint(20, 2000)):
    print(Card("4", "♠"))

print("Obiectie create:", Card.counter)