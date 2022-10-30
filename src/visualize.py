from datetime import datetime
from data.sql import get_records
from fns.charts import generate_chart
                
if __name__ == '__main__':
    records = get_records("XAUUSD", "H1", datetime(2021,1,4), datetime(2021,1,6))
    generate_chart(records)
