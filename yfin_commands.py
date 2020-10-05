import logging
import yfinance as yf
import re

logger = logging.getLogger('Botty_Logger')
yfin_command_pattern = re.compile(r"""\{(yfin_.*)\}""", re.X)
yfin_price_cache = {}


def get_price(ticker):
    logger.info('Executing get_price command')
    if ticker in yfin_price_cache:
        logging.debug('Reaching into the yfin cache for {ticker}'.format(ticker=ticker))
        return yfin_price_cache.get(ticker)
    else:
        data = yf.Ticker(ticker)
        price = data.history(period='1d')['High'][0]
        if len(yfin_price_cache) < 10:
            logger.debug('Putting {ticker} into the yfin cache'.format(ticker=ticker))
            yfin_price_cache[ticker] = price
        else:
            logger.debug('Clearing the yfin cache and starting fresh with {ticker}'.format(ticker=ticker))
            yfin_price_cache.clear()
            yfin_price_cache[ticker] = price
        return price


def execute_yfin_command(command, args):
    if command == 'yfin_get_price':
        return get_price(args[0])
