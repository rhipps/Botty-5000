import yfinance as yf
import re

yfin_command_pattern = re.compile(r"""\{(yfin_.*)\}""", re.X)
yfin_price_cache = {}


def get_price(ticker):
    if ticker in yfin_price_cache:
        print('Reaching into the yfin cache for {}'.format(ticker))
        return yfin_price_cache.get(ticker)
    else:
        data = yf.Ticker(ticker)
        price = data.history(period='1d')['High'][0]
        if len(yfin_price_cache) < 10:
            print('Putting {} into the yfin cache'.format(ticker))
            yfin_price_cache[ticker] = price
        else:
            print('Clearing the yfin cache and starting fresh with {}'.format(ticker))
            yfin_price_cache.clear()
            yfin_price_cache[ticker] = price
        return price


def execute_yfin_command(command, args):
    if command == 'yfin_get_price':
        return get_price(args[0])