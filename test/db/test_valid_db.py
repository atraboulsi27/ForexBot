import sys, os
sys.path.append(os.path.join(sys.path[0],'../..'))
from src.config import symbols, timeframes, timezone, date_to
from datetime import datetime
from src.API.api import get_data
from src.data.config import mycol, client
from src.data.transform import transform_record
import pytest

#fixture of all the data we have
#@TODO: must create a resource file and print that data in the file and read it here

@pytest.fixture
def candles_api():
    records_api =[]
    date_from = datetime(2021, 12, 1, tzinfo=timezone)
    for symbol in symbols:
        records_api.extend(get_data(symbol, timeframes[0], date_from, date_to))
        records_api.extend(get_data(symbol, timeframes[1], date_from, date_to))
    date_from = datetime(2021, 10, 1, tzinfo=timezone)
    for symbol in symbols:
        records_api.extend(get_data(symbol, timeframes[2], date_from, date_to))
        records_api.extend(get_data(symbol, timeframes[3], date_from, date_to))
    date_from = datetime(2021, 7, 1, tzinfo=timezone)
    for symbol in symbols:
        records_api.extend(get_data(symbol, timeframes[4], date_from, date_to))
    date_from = datetime(2021, 1, 1, tzinfo=timezone)
    for symbol in symbols:
        records_api.extend(get_data(symbol, timeframes[5], date_from, date_to))
        records_api.extend(get_data(symbol, timeframes[6], date_from, date_to))
    return records_api

@pytest.fixture
def candles_realdb():
    return list(mycol.find({}))

@pytest.fixture
def candles_testdb():
    mydb = client["test_forexdb"]
    return mydb["candles"]


#fixture that takes info and returns record from db

def test_number_of_records(candles_api, candles_testdb):
    count_api = len(candles_api)
    count_realdb = mycol.count_documents({})
    count_testdb = candles_testdb.count_documents({})

    assert count_api == count_realdb
    assert count_api == count_testdb

# def test_records(candles_api, candles_testdb):
    
#     data_api = []
#     for record in candles_api:
#         trans_record = transform_record(record, "x","x")
#         for e in ["Symbol", "Timeframe"]:
#             trans_record.pop(e)
#         data_api.append(trans_record)

#     # data_db = list(mycol.find({}, {"_id": 0, "Symbol": 0, "Timeframe": 0}))
#     # data_testdb = list(candles_testdb.find({}, {"_id": 0, "Symbol": 0, "Timeframe": 0}))

#     for record in data_api:
#         try:
#             assert len((list(mycol.find(record)))) == 1
#         except AssertionError:
#             print(list(mycol.find(record)))

    

#     # assert data_api == list(data_db)
#     # assert data_api == list(data_testdb)




#idea: pass over each candle in api, transform and then find in db with count, if count > 2 add it to array print array
# def test_api_record_in_db(candles_api):

#     candles_db = []
#     for candle_api in candles_api:
        
#         search = transform_record(candle_api, "x","x")
#         for e in ["Symbol", "Timeframe"]:
#             search.pop(e)
#         found = list(mycol.find(search))
#         #not found case
#         if len(found) == 0:
#             print("Not found: {} ==> {}\n".format(search, candle_api))
#         #if duplicate
#         if len(found) > 1:
#             print("Duplicate: {} ==> {}\n".format(search, candle_api))
#             print("Number of occurences: {}\n".format(len(found)))
#             candles_db.append(found[0])
#         #one instance found <- wanted result
#         if len(found) == 1:
#             candles_db.append(found[0])
