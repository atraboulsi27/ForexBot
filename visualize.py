import MetaTrader5 as mt5
from src.API.api import get_data
from config import date_from, date_to, symbols, timeframes
import pandas as pd
from datetime import datetime

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)

rates = get_data(symbols[0], timeframes[0], date_from, date_to)


rates_frame = pd.DataFrame(rates)
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
print(datetime.utcfromtimestamp(rates[1][0]).strftime('%Y-%m-%d %H:%M:%S'))