import matplotlib.pyplot as plt
import urllib.request,json
from alpha_vantage.timeseries import TimeSeries
from pandas_datareader import data
import sys
import pandas as pd
import datetime
from .models import Stock


api_key = '1JOT4RUOO2W2OGA1'
ticker = "AAL"
base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAL&apikey={}"

def aal_data():
    url_string = base_url.format(api_key)
    with urllib.request.urlopen(url_string) as url:
        data_x=url.read().decode('utf-8')
        response=json.loads(data_x)

        data_y=response['Time Series (Daily)']
        
