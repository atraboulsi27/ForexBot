#run this file to get the historical data needed
from datetime import datetime
from config import symbols, timeframes, timezone, date_to
from API.api import get_data
from data.sql import get_latest_time, upsert_records, insert_records
from data.transform import transform_record
from time import time

# def get_m5():
#     date_from = datetime(2021, 12, 1, tzinfo=timezone)
#     for symbol in symbols:
#         rates = get_data(symbol, timeframes[0], date_from, date_to)
#         transformed = []
#         for rate in rates:
#             transformed.append(transform_record(rate, symbol, "M5"))
#         insert_records(transformed)

# def get_m15():
#     date_from = datetime(2021, 12, 1, tzinfo=timezone)
#     for symbol in symbols:
#         rates = get_data(symbol, timeframes[1], date_from, date_to)
#         transformed = []
#         for rate in rates:
#             transformed.append(transform_record(rate, symbol, "M15"))
#         insert_records(transformed)

# def get_m30():
#     date_from = datetime(2021, 10, 1, tzinfo=timezone)
#     for symbol in symbols:
#         rates = get_data(symbol, timeframes[2], date_from, date_to)
#         transformed = []
#         for rate in rates:
#             transformed.append(transform_record(rate, symbol, "M30"))
#         insert_records(transformed)

# def get_h1():
#     date_from = datetime(2021, 10, 1, tzinfo=timezone)
#     for symbol in symbols:
#         rates = get_data(symbol, timeframes[3], date_from, date_to)
#         transformed = []
#         for rate in rates:
#             transformed.append(transform_record(rate, symbol, "H1"))
#         insert_records(transformed)

# def get_h4():
#     date_from = datetime(2021, 7, 1, tzinfo=timezone)
#     for symbol in symbols:
#         rates = get_data(symbol, timeframes[4], date_from, date_to)
#         transformed = []
#         for rate in rates:
#             transformed.append(transform_record(rate, symbol, "H4"))
#         insert_records(transformed)

# def get_d1():
#     date_from = datetime(2021, 1, 1, tzinfo=timezone)
#     for symbol in symbols:
#         rates = get_data(symbol, timeframes[5], date_from, date_to)
#         transformed = []
#         for rate in rates:
#             transformed.append(transform_record(rate, symbol, "D1"))
#         insert_records(transformed)

# def get_w1():
#     date_from = datetime(2021, 1, 1, tzinfo=timezone)
#     for symbol in symbols:
#         rates = get_data(symbol, timeframes[6], date_from, date_to)
#         transformed = []
#         for rate in rates:
#             transformed.append(transform_record(rate, symbol, "W1"))
#         insert_records(transformed)

def retrieve_latest_data():
    for symbol in symbols:
        for timeframe in timeframes:
            doc = get_latest_time(symbol, timeframe)
            date = doc["Date"]
            date_from_localized = timezone.localize(date)
            candles = get_data(symbol, timeframe, date_from_localized, date_to)
            #remove first element since it overlaps with the one in the database
            candles = candles[1:]

            if candles != []:
                transformed = []
            
                for candle in candles:
                    transformed.append(transform_record(candle, symbol, timeframe))
            
                insert_records(transformed)



                
# if __name__ == '__main__':
#     start = time()
#     print("Fetching and inserting data\n")
#     get_m5()
#     get_m15()
#     get_m30()
#     get_h1()
#     get_h4()
#     get_d1()
#     get_w1()
#     end = time()
#     print("Data fetch and insertion done, time taken is {}\n".format(end - start))