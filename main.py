from config import date_from, date_to, symbols, timeframes
from src.API.api import get_data
from src.data.sql import insert_records
from src.data.transform import transform_record

rates = get_data(symbols[0], timeframes[0], date_from, date_to)

transformed = []
for rate in rates:
    transformed.append(transform_record(rate, symbols[0], "M5"))

insert_records(transformed)