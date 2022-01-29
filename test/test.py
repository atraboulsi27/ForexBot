from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# # import the 'pandas' module for displaying data obtained in the tabular form
# import pandas as pd
# pd.set_option('display.max_columns', 500) # number of columns to be displayed
# pd.set_option('display.width', 1500)      # max table width to display
# # import pytz module for working with time zone
# import pytz
 
# # establish connection to MetaTrader 5 terminal
# if not mt5.initialize():
#     print("initialize() failed, error code =",mt5.last_error())
#     quit()
 
# # set time zone to UTC
# timezone = pytz.timezone("Etc/UTC")
# # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
# utc_from = datetime(2022, 1, 26, tzinfo=timezone)
# # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
# rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H1, utc_from, 10)
 
# # shut down connection to the MetaTrader 5 terminal
# mt5.shutdown()
# # display each element of obtained data in a new line
# print("Display obtained data 'as is'")
# for rate in rates:
#     print(rate)
 
# # create DataFrame out of the obtained data
# rates_frame = pd.DataFrame(rates)
# # convert time in seconds into the datetime format
# rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
                           
# # display data
# print("\nDisplay dataframe with data")
# print(rates_frame)  

# # establish connection to the MetaTrader 5 terminal
# if not mt5.initialize():
#     print("initialize() failed, error code =",mt5.last_error())
#     quit()
 
# get the number of financial instruments
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# symbols=mt5.symbols_total()
# if symbols>0:
#     print("Total symbols =",symbols)
# else:
#     print("symbols not found")
 # get all symbols
symbols=mt5.symbols_get()
print('Symbols: ', len(symbols))
count=0
# display the first five ones
for s in symbols:
    count+=1
    print("{}. {}".format(count,s.name))
    if count==5: break
print()
 
# get symbols containing RU in their names
ru_symbols=mt5.symbols_get("*RU*")
print('len(*RU*): ', len(ru_symbols))
for s in ru_symbols:
    print(s.name)
print()
 
# get symbols whose names do not contain USD, EUR, JPY and GBP
group_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))
for s in group_symbols:
    print(s.name,":",s)
    
# shut down connection to the MetaTrader 5 termina