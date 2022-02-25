#contains all the sql queries needed
from pymongo import MongoClient
from pymongo import ReplaceOne

db_username = "user123"
db_password = "D8MwIKh5gLL09imk"
db = "forexdb" 
client = MongoClient("mongodb+srv://"+db_username+":"+db_password+"@forexdb.2sf98.mongodb.net/"+db+"?retryWrites=true&w=majority")
mydb = client["forexdb"]
mycol = mydb["candles"]

# takes an array of one record shaped by the transform fucntion
def insert_records(records):
    requests = []
    for record in records:
        requests.append(ReplaceOne(record, record, upsert=True))
    if len(records) == len(requests):
        mycol.bulk_write(requests)

#all optional args, query by arg each time one is found ex. by date, by symbol
# def retrieve_records()



