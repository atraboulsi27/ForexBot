from src.data.config import mycol
from json import load
mydata = mycol.find({})
print(list(mydata))