import pytz
from datetime import datetime
import MetaTrader5 as mt5

timezone = pytz.timezone("Etc/UTC")



symbols = ["EURUSD", "EURGBP"]

timeframes = [mt5.TIMEFRAME_M5, mt5.TIMEFRAME_M15 ,mt5.TIMEFRAME_M30, mt5.TIMEFRAME_H1, mt5.TIMEFRAME_H4, mt5.TIMEFRAME_D1, mt5.TIMEFRAME_W1]

date_from = datetime(2021, 1, 1, tzinfo=timezone)
date_to = datetime(2022, 1, 1, tzinfo=timezone)