import pymongo
from pymongo import ReplaceOne

# takes an array of one record shaped
def insert_records(records):
    db_username = "user123"
    db_password = "D8MwIKh5gLL09imk"
    db = "forexdb" 
    client = pymongo.MongoClient("mongodb+srv://"+db_username+":"+db_password+"@forexdb.2sf98.mongodb.net/"+db+"?retryWrites=true&w=majority")
    mydb = client["forexdb"]
    mycol = mydb["candles"]

    requests = []
    for record in records:
        requests.append(ReplaceOne(record, record, upsert=True))

    if len(records) == len(requests):
        mycol.bulk_write(requests)

# mydict = { "name": "John", "address": "Highway 37", "b": "c" }
# requests = [ReplaceOne(mydict,  { "name": "John", "address": "Highway 37"}, upsert = True)]


