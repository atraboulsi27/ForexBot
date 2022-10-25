#run this file to get the historical data needed
from datetime import datetime
from config import symbols, timeframes, timezone, date_to, timeframes_string
from API.api import get_data
from data.sql import get_latest_date, upsert_records, insert_records
from data.transform import transform_record
from time import time

def retrieve_latest_data():
    for symbol in symbols:
        #for time frame for each symbol (time frame string, time frame obj) combo
        for t_s, t in zip(timeframes_string, timeframes):
            #get latest date
            date = get_latest_date(symbol, t_s)
            #transform it
            date_from_localized = timezone.localize(date)
            # use it as date from
            candles = get_data(symbol, t, date_from_localized, date_to)
            #remove first element since it overlaps with the one in the database
            candles = candles[1:]

            transformed = []
            for candle in candles:
                transformed.append(transform_record(candle, symbol, t_s))
        
            insert_records(transformed)

                
if __name__ == '__main__':
    start = time()
    print("Fetching and inserting data\n")
    retrieve_latest_data()
    end = time()
    print("Data fetch and insertion done, time taken is {}\n".format(end - start))
