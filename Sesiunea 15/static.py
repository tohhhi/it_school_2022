class Ticket:

    def __init__(self, price):
        # Atribute de instanta
        self.price = price

    # metode de instanta
    def get_price_w_taxes(self):
        return self.price + self.price * Ticket.get_tva_ratio()

    # definire metoda statica = metoda de clasa 
    @staticmethod
    def get_tva_ratio(): # metodele statice nu au nevoie de self 
        return 0.19

    @staticmethod
    def stm():
        print("TVA:", Ticket.get_tva_ratio())


#instantiere
tk = Ticket(100)

# tk = obiect = instanta
tk.stm()
Ticket.stm()

#print(Ticket.get_tva_ratio())