# add imports, if necessary
from currency_converter import convert
from exchange_rates import EXCHANGE_RATES

class BankAccount:

    def __init__(self, currency="CHF"):
        if currency == "":
            raise Warning
        elif currency not in EXCHANGE_RATES.keys():
            raise Warning

        self.__balance = 0
        self.__currency = currency

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount, currency="CHF"):
        if currency == "":
            raise Warning
        elif currency not in EXCHANGE_RATES.keys():
            raise Warning
        elif not type(amount) == int and not type(amount) == float:
            raise Warning
        elif not amount > 0:
            raise Warning
        else:
            if self.__currency == currency:
                self.__balance += amount
            else:
                withdrawal = convert(amount, currency, self.__currency)
                self.__balance += withdrawal

    def withdraw(self, amount, currency="CHF"):
        print(type(amount))
        if currency == "":
            raise Warning
        elif currency not in EXCHANGE_RATES.keys():
            raise Warning
        elif not type(amount) == int and not type(amount) == float:
            raise Warning
        elif not amount > 0:
            raise Warning
        else:

            if self.__currency == currency:
                if self.__balance >= amount:
                    self.__balance -= amount
                else:
                    raise Warning

            else:
                withdrawal = convert(amount, currency, self.__currency)
                if self.__balance >= withdrawal:
                    self.__balance -= withdrawal
                else:
                    raise Warning
