from django.shortcuts import render
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from pandas_datareader import data
import sys
import pandas as pd
import datetime

from django.template import RequestContext
import urllib.request,json
api_key = '1JOT4RUOO2W2OGA1'
ticker = "AAL"
base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAL&apikey={}"

def home(request):

    title='welcome to neural finance system'
    url_string = base_url.format(api_key)
    with urllib.request.urlopen(url_string) as url:
        data_x=url.read().decode('utf-8')
        response=json.loads(data_x)

        data_y=response['Time Series (Daily)']



        print("its worked")






    return render (request,'home.html',{"title":title,"data_y":data_y})
