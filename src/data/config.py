from pymongo import MongoClient

db_username = "user123"
db_password = "D8MwIKh5gLL09imk"
db = "forexdb"
#online atlas 
client = MongoClient("mongodb+srv://"+db_username+":"+db_password+"@forexdb.2sf98.mongodb.net/"+db+"?retryWrites=true&w=majority")
#local client
# client = MongoClient("mongodb://localhost:27017")
mydb = client["forexdb"]
mycol = mydb["candles"]