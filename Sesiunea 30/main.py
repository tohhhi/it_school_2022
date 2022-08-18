import random
from datetime import datetime
from tkinter import NONE

class VaultLockedException(Exception):
    def __init__(self) -> None:
        super().__init__("Seif blocat! Pin introdus gresit de 3 ori!")


class NotInServiceModeException(Exception):
    def __init__(self) -> None:
        super().__init__("ATM-ul nu este in modul service!")


class InsufficientFundsException(Exception):
    def __init__(self) -> None:
        super().__init__("Fonduri insuficiente!")

class WrongPinException(Exception):
    def __init__(self) -> None:
        super().__init__("Cod PIN gresit!")

class Card:
    def __init__(self, owner_name, pin) -> None:
        self.number = random.sample([str(x) for x in range(10)], 16)
        self.expire_date = datetime(2030, 8, 1)
        self.security_code = random.randint(100, 1000)
        self.owner = owner_name
        self.__balance = 0
        self.pin = pin

    def get_balance(self):
        return self.__balance

    def add_money(self, value):
        self.__balance += value

    def check_pin(self, pin):
        return pin == self.__pin
    
    def withdraw(self, amount):
        self.__balance -= amount

class ATM:
    def __init__(self) -> None:
        self.__vault = {1: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0}
        self.__service_mode = False
        self.pin = "8464903"
        self.__retry_counter = 0

    def fill(self, banknote, count):
        if not self.__service_mode:
            raise NotInServiceModeException()

        if not isinstance(banknote, int) and banknote not in self.__vault.keys():
            raise ValueError(f"Bancnota neacceptata: {banknote}")

        if not isinstance(count, int) and count < 0:
            raise ValueError(f"Numar invalid de bancnote: {count}")

        self.__vault.update({banknote: count})

    def withdraw(self, card: Card, pin: int, amount):
        if card.check_pin(pin):
            if card.get_balance() >= amount:
                card.withdraw(amount)
            else:
                raise InsufficientFundsException()
        else:
            raise WrongPinException()


    def authenticate_service_man(self, pin):
        if self.__retry_counter > 3:
            raise VaultLockedException()

        if pin == self.pin:
            self.__service_mode = True
            self.__retry_counter = 0
        else:
            self.__retry_counter += 1

    def logout_service_man(self):
        self.__service_mode = False