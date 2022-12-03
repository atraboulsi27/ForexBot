import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

#create function that returns the missing dates from df 
def generate_chart(records, start_date, end_date):
    df = pd.DataFrame(records)

    # df_dates = df['Date'].tolist()
    # df_dates_formatted = [date.strftime("%Y-%m-%d") for date in df_dates]
    # all_dates = pd.date_range(start_date, end_date - timedelta(days=1), freq = "H").tolist()

    # missing_dates = []

    # for date in all_dates:
    #     formatted_date = date.strftime("%Y-%m-%d")
    #     if formatted_date not in df_dates_formatted:
    #         missing_dates.append(date)
    
    # print(df_dates)
    # print(missing_dates)
    chart = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])

    # chart.update_xaxes(rangebreaks=[dict(values=missing_dates)])
    chart.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])
    chart.show()