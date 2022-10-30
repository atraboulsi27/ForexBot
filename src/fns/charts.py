import plotly.graph_objects as go
import pandas as pd

def generate_chart(records):
    df = pd.DataFrame(records)
    print(df)
    chart = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])

    chart.show()