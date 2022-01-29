# Should have the function that takes the parameters
# and gets the historical data


import MetaTrader5 as mt5


def get_data(symbol, timeframe, date_from, date_to):
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()
    else:
        mt5.copy_rates_range(symbol, timeframe, date_from, date_to)

# def update_data_latest():

#check db for latest date, take it as date_from and take current date as date_to

