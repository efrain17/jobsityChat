"""This module manage stock model"""
import io
import pandas as pd
import requests


def get(stock_code):
    """Get stock from stooq"""
    url = f'https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv'
    stock_data = requests.get(url).content
    stock_data = pd.read_csv(io.StringIO(stock_data.decode('utf-8')))
    return stock_data['Open'].iloc[0]
