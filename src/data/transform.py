from datetime import datetime

def transform_record(record, symbol, timeframe):
    return {"Symbol": symbol,
            "Timeframe": timeframe,
            "Date": datetime.utcfromtimestamp(record[0]).strftime('%Y-%m-%d %H:%M:%S'),
            "Open": record[1],
            "High": record[2],
            "Low": record[3],
            "Close": record[4]}