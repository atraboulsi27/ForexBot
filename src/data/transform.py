#contains the functions that shape the fetched record from api before injecting into db
from datetime import datetime

def transform_record(record, symbol, timeframe):
    return {"Symbol": symbol,
            "Timeframe": timeframe,
            "Date": datetime.utcfromtimestamp(record[0]),
            "Open": record[1],
            "High": record[2],
            "Low": record[3],
            "Close": record[4]}