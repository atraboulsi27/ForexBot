#contains all the sql queries needed
from pymongo import ReplaceOne,InsertOne
from .config import mycol

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

#returns a dictionary of the symbol, timeframe and date of the document with the latest date
def get_latest_time(symbol, timeframe):
    pipeline = [{"$match": { "Symbol": symbol , "Timeframe": timeframe } },
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
                            "_id" : { "s": "$Symbol","t": "$Timeframe"},
                            "maxDate": { "$max": "$Date" }
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
    result = list(mycol.aggregate(pipeline, allowDiskUse = True))[0]
    # result["Date"] = result["Date"].strftime('%Y-%m-%d %H:%M:%S')
    return result         

#all optional args, query by arg each time one is found ex. by date, by symbol
# def retrieve_records()



