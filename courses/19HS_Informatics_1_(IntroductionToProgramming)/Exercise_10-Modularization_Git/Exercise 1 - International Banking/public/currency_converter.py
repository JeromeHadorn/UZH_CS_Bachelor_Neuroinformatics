# add imports, if necessary
from exchange_rates import EXCHANGE_RATES

def convert(amount, from_currency, to_currency):

    if from_currency == "" or to_currency == "":
        raise Warning
    if not from_currency in EXCHANGE_RATES.keys():
        raise Warning
    if not to_currency in EXCHANGE_RATES.keys():
        raise Warning

    if not type(amount) == int and not type(amount) == float:
        raise Warning
    if not amount > 0:
        raise Warning

    exchangeRate = None
    directionFlag = None

    if to_currency in EXCHANGE_RATES[from_currency]:
        exchangeRate = EXCHANGE_RATES[from_currency][to_currency]
        directionFlag = True
    else:
        exchangeRate = EXCHANGE_RATES[to_currency][from_currency]
        directionFlag = False

    if directionFlag:
        return amount * exchangeRate
    else:
        return amount * (1/exchangeRate)
