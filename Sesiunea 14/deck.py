from random import shuffle


class Card:
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol

    def __str__(self):
        return self.number + self.symbol

    def __repr__(self):
        return self.__str__()



class Deck:

    def __init__(self):
        self.__AVAILABLE_SYMBOLS = ("♠", "♥", "♦", "♣")
        self.__cards = []
        
        self.__generate_cards()

    def get_cards(self, number):
        r_cards = []
        for i in range(number):
            r_cards.append(self.__cards.pop())
        return r_cards

    def __len__(self):
        return len(self.__cards)

      
    
    def shuffle(self):
        shuffle(self.__cards)
        return self.__cards


    def __generate_available_numbers(self):
        a_n = []
        for i in range(2, 11):
            a_n.append(str(i))
        a_n.extend(["A", "J", "Q", "K"])
        return tuple(a_n)
    
    def __generate_cards(self):
        for i in self.__generate_available_numbers():
            for j in self.__AVAILABLE_SYMBOLS:
                self.__cards.append(Card(i, j))

    def get_all_cards(self):
        return self.get_cards(52)



deck = Deck()

#print(deck.get_all_cards())

print(deck.shuffle())

print(len(deck))
