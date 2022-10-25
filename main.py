from data.db_config import mycol
from json import load
mydata = mycol.find({})
print(list(mydata))