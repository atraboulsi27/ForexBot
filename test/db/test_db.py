import sys, os

sys.path.append(os.path.join(sys.path[0], '../..'))
from data.db_config import client
from src.config import symbols, timeframes
from pymongo import ASCENDING
import time
import pytest
import random
from datetime import datetime


@pytest.fixture
def testcol():
    mydb = client["test_forexdb"]
    return mydb["candles"]


def test_index_time(testcol):
    # ONE INDEX
    testcol.create_index([("Symbol", ASCENDING)])
    start = time.time()
    list(testcol.find({"Symbol": random.choice(symbols),
                       "Timeframe": random.choice(timeframes)}))
    end = time.time()
    time_with_one_index = end - start
    testcol.drop_index("Symbol_1")

    # NO INDEX
    start = time.time()
    list(testcol.find({"Symbol": random.choice(symbols),
                       "Timeframe": random.choice(timeframes)}))
    end = time.time()
    time_without_index = end - start

    # COMPOUND INDEX
    testcol.create_index([("Symbol", ASCENDING), ("Timeframe", ASCENDING)])
    start = time.time()
    list(testcol.find({"Symbol": random.choice(symbols),
                       "Timeframe": random.choice(timeframes)}))
    end = time.time()
    time_with_compound_index = end - start
    testcol.drop_index("Symbol_1_Timeframe_1")

    # results: without index 0.3, with one index 0.03, with compound index 0.0009
    assert time_without_index > time_with_one_index
    assert time_with_one_index > time_with_compound_index


def test_latest_date(testcol):
    init_count_docs = testcol.count_documents({})
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    symbol = random.choice(symbols)
    timeframe = random.choice(timeframes)
    doc = {"Symbol": symbol,
           "Timeframe": timeframe,
           "Date": current_date,
           "Open": 0.1,
           "High": 0.1,
           "Low": 0.1,
           "Close": 0.1}

    testcol.insert_one(doc)
    after_add_count_docs = testcol.count_documents({})

    pipeline = [{"$match": {"Symbol": symbol, "Timeframe": timeframe}},
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
                            "_id": {"s": "$Symbol", "t": "$Timeframe"},
                            "maxDate": {"$max": "$Date"}
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
    latest_date = list(testcol.aggregate(pipeline, allowDiskUse=True))[0]["Date"].strftime('%Y-%m-%d %H:%M:%S')

    testcol.delete_one(doc)
    after_del_count_docs = testcol.count_documents({})

    assert after_add_count_docs == (init_count_docs + 1)
    assert after_del_count_docs == init_count_docs
    assert current_date == latest_date
