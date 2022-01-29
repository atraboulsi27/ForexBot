import pymongo

client = pymongo.MongoClient("mongodb+srv://user123:<password>@forexdb.2sf98.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test