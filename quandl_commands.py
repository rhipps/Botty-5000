import quandl
import re
import json

with open('./props.json') as props_file:
    props = json.load(props_file)

quandl_command_pattern = re.compile(r"""\{(quandl_.*)\}""", re.X)
quandl.ApiConfig.api_key = props['quandl-key']
quandl_price_cache = {}


def get_price(quandl_code):
    if quandl_code in quandl_price_cache:
        print('Reaching into the quandl cache for {}'.format(quandl_code))
        return quandl_price_cache.get(quandl_code)
    else:
        data = quandl.get(quandl_code, rows=1)
        price = data.values[0][0]
        if len(quandl_price_cache) < 10:
            print('Putting {} into the quandl cache'.format(quandl_code))
            quandl_price_cache[quandl_code] = price
        else:
            print('Clearing the quandl cache and starting fresh with {}'.format(quandl_code))
            quandl_price_cache.clear()
            quandl_price_cache[quandl_code] = price
        return price


def execute_quandl_command(command, args):
    if command == 'quandl_get_price':
        return get_price(args[0])
