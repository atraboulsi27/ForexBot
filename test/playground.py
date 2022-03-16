import sys, os
sys.path.append(os.path.join(sys.path[0],'..'))
from src.data.config import client
import pymongo
from src.API.api import get_data
from src.data.sql import get_latest_time
from datetime import datetime
from src.config import timezone, timeframes

doc = get_latest_time("AUDJPY", "M5")
date = doc["Date"]
date_from_localized = timezone.localize(date)
date_to_localized = datetime.now(timezone)
data = (get_data("AUDJPY", timeframes[3], date, datetime.now()))
data2 = data[1:]
#the date_from is included

print(data2==data)














# pipeline1 = [
#    {
#       "$project": {
#          "DateFormatted": {"$toDate": "$Date"}
#       }
#    },
#    {
#       "$sort": {
#          "DateFormatted": pymongo.DESCENDING
#       }
#    }]

# symbol = "AUDJPY"
# timeframe = "M30"
# pipeline2 = [{"$match": { "Symbol": symbol , "Timeframe": timeframe } },
#                 {
#                     "$project": {
#                         "Date": {"$toDate": "$Date"},
#                         "Symbol": 1,
#                         "Timeframe": 1,
#                     }
#                 }, 
#                 {
#                     "$group":
#                         {
#                             "_id" : { "s": "$Symbol","t": "$Timeframe"},
#                             "maxDate": { "$max": "$Date" }
#                         }
#                 },
#                 {
#                     "$project":
#                         {
#                             "_id": "$type",
#                             "Symbol": "$_id.s",
#                             "Timeframe": "$_id.t",
#                             "Open": "$_id.Open",
#                             "Date": "$maxDate",
#                         }
#                 }
#                 ]
#    # {
#    #    "$project": {
#    #       "_id" : { "_id": "$_id", "Symbol": "$Symbol", "Timeframe": "$Timeframe", "Open": "$Open" }
#    #    }}]
# mydb = client["test_forexdb"]
# mycol = mydb["candles"]

# # results = list(mycol.aggregate(pipeline1, allowDiskUse = True))
# results = list(mycol.aggregate(pipeline2, allowDiskUse = True))[0]
# #the resultant is datetime using projtec, script if absolutely possible
# print(results)