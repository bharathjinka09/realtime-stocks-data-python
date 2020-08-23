from nsetools import Nse
from pprint import pprint

nse = Nse()

try:
    symbol = input("Enter Stock Symbol: ")
    quote = nse.get_quote(symbol)

    pprint(quote)

    pprint(quote["totalSellQuantity"])
except Exception as e:
    print("Please enter a valid stock symbol")

