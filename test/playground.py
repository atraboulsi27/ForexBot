import pandas as pd

dates = pd.date_range("2021-01-01", "2021-01-10")

for date in dates:
    print(date)