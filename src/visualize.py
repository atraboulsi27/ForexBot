from datetime import datetime
from data.sql import get_records
from fns.charts import generate_chart
from populate import retrieve_latest_data
                
if __name__ == '__main__':
    # retrieve_latest_data()
    symbol = input("Please input symbol i.e. XAUUSD: ")
    timeframe = input("Please input timeframes i.e. H1: ")
    start_year = int(input("Please input start year i.e. 2021 (only use as old as 2021 for now): "))
    start_month = int(input("Please input start month i.e. 1,2,3..12 : "))
    start_day = int(input("Please input start day i.e. 1,2,3..31 : "))
    end_year = int(input("Please input end year i.e. 2021 (only use as old as 2021 for now): "))
    end_month = int(input("Please input end month i.e. 1,2,3..12 : "))
    end_day = int(input("Please input end day i.e. 1,2,3..31 : "))
    start_date = datetime(start_year,start_month,start_day)
    end_date = datetime(end_year,end_month,end_day)
    records = get_records(symbol, timeframe, start_date, end_date)
    generate_chart(records, start_date, end_date)
