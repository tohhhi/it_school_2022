
import unittest
from unittest import mock

from main import ATM, InsufficientFundsException, WrongPinException
# TestCase

class TestConstructor(unittest.TestCase):

    def test_pin_value(self):
        atm = ATM()
        self.assertEqual(atm.pin,"8464903") 


class TestWithdraw(unittest.TestCase):

    def test_pin_ok_amount_ok(self):
        atm = ATM()
        am = 100
        card = mock.Mock()
        card.check_pin.return_value = True
        card.get_balance.return_value = am
       
        atm.withdraw(card, 0, am)

        card.withdraw.assert_called()
        # atm.withdraw()

    def test_pin_ok_no_balance(self):
        atm = ATM()
        am = 100
        card = mock.Mock()
        card.check_pin.return_value = True
        card.get_balance.return_value = 80
       
        with self.assertRaises(InsufficientFundsException):
            atm.withdraw(card, 0 , am)


    def test_pin_nok(self):
        atm = ATM()
        am = 100
        card = mock.Mock()
        card.check_pin.return_value = False
        card.get_balance.return_value = 80
       
        with self.assertRaises(WrongPinException):
            atm.withdraw(card, 0 , am)



# python -m unittest -vv tests.test_atm