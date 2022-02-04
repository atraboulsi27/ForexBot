from datetime import datetime

def transform_record(record, symbol, timeframe):
    return {"S": symbol,
            "TF": timeframe,
            "D": datetime.utcfromtimestamp(record[0]).strftime('%Y-%m-%d %H:%M:%S'),
            "O": record[1],
            "H": record[2],
            "L": record[3],
            "C": record[4]}