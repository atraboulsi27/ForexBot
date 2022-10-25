# contains all the sql queries needed
from datetime import datetime
from pymongo import ReplaceOne, InsertOne
from .db_config import mycol


# takes an array of one record shaped by the transform function
def insert_records(records):
    requests = []
    for record in records:
        requests.append(InsertOne(record))
    if len(records) == len(requests):
        mycol.bulk_write(requests)


def insert_record(record):
    mycol.insert_one(record)


def upsert_records(records):
    requests = []
    for record in records:
        requests.append(ReplaceOne(record, record, upsert=True))
    if len(records) == len(requests):
        mycol.bulk_write(requests)


# returns the date of the latest document, returns 2021-01-01 if there are no documents (fresh db())
def get_latest_date(symbol, timeframe):
    pipeline = [{"$match": {"Symbol": symbol, "Timeframe": timeframe}},
                {
                    "$project": {
                        "Date": {"$toDate": "$Date"},
                        "Symbol": 1,
                        "Timeframe": 1,
                    }
                },
                {
                    "$group":
                        {
                            "_id": {"s": "$Symbol", "t": "$Timeframe"},
                            "maxDate": {"$max": "$Date"}
                        }
                },
                {
                    "$project":
                        {
                            "_id": "$type",
                            "Symbol": "$_id.s",
                            "Timeframe": "$_id.t",
                            "Open": "$_id.Open",
                            "Date": "$maxDate",
                        }
                }
                ]
    db_record = list(mycol.aggregate(pipeline, allowDiskUse=True))
    if db_record == []:
        return datetime(2021,1,1,00,00,00)
    else:  
        return list(mycol.aggregate(pipeline, allowDiskUse=True))[0]["Date"]