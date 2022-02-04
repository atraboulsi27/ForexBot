import pytz
from datetime import datetime
import MetaTrader5 as mt5

timezone = pytz.timezone("Etc/UTC")


symbols = ["EURUSD", "EURGBP"]

# M5 and M15 => 12 2021
# M30 and H1 => 10 2021
# H4 => 07 2021 
# D1 and W1 => 01 2021
timeframes = [mt5.TIMEFRAME_M5, mt5.TIMEFRAME_M15 ,mt5.TIMEFRAME_M30, mt5.TIMEFRAME_H1, mt5.TIMEFRAME_H4, mt5.TIMEFRAME_D1, mt5.TIMEFRAME_W1]

date_from = datetime(2021, 12, 1, tzinfo=timezone)
date_to = datetime(2022, 2, 4, tzinfo=timezone)


