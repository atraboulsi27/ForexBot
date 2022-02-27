#contains all the sql queries needed
from pymongo import ReplaceOne,InsertOne
from config import mycol

# takes an array of one record shaped by the transform fucntion
def insert_records(records):
    requests = []
    for record in records:
        requests.append(InsertOne(record))
    if len(records) == len(requests):
        mycol.bulk_write(requests)

def upsert_records(records):
    requests = []
    for record in records:
        requests.append(ReplaceOne(record, record, upsert=True))
    if len(records) == len(requests):
        mycol.bulk_write(requests)

#all optional args, query by arg each time one is found ex. by date, by symbol
# def retrieve_records()



