from pytz import timezone as tz
from datetime import datetime
import MetaTrader5 as mt5

timezone = tz("Etc/UTC")

#29 pairs
symbols = ["XAUUSD", "USDJPY", "USDCAD", "USDCHF", "EURUSD", "EURJPY", "EURGBP", "EURAUD", "EURNZD", "EURCAD", "EURCHF", "GBPUSD", "GBPJPY", "GBPAUD", "GBPNZD", "GBPCAD", "GBPCHF", "AUDUSD", "AUDJPY", "AUDNZD", "AUDCAD", "AUDCHF", "NZDUSD", "NZDJPY", "NZDCAD", "NZDCHF", "CADJPY", "CADCHF", "CHFJPY"]

#H1 => 10 2021
# H4 => 07 2021 
# D1 and W1 => 01 2021
timeframes = [mt5.TIMEFRAME_H1, mt5.TIMEFRAME_H4, mt5.TIMEFRAME_D1, mt5.TIMEFRAME_W1]
timeframes_string = ["H1","H4","D1","W1"]
date_to = datetime.now(timezone)


