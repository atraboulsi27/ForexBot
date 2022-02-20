#contains the calls for api

import MetaTrader5 as mt5

def get_data(symbol, timeframe, date_from, date_to):
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()
    else:
        return mt5.copy_rates_range(symbol, timeframe, date_from, date_to)