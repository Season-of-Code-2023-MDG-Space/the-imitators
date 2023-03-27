from django.shortcuts import render
import yfinance as yf
from .models import *
from rest_framework.generics import ListCreateAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json
import pandas as pd
from rest_framework.parsers import JSONParser
import sqlite3
import math
import pandas_datareader as web
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# from keras.models import Sequential
# from keras.layers import Dense, LSTM
# import tensorflow.compat.v2 as tf
recent_ticker = ""

# Create your views here.
@api_view(['GET','POST'])
def TickerList(request):

    if(request.method =='GET'):
        ticker=Ticker.objects.all()
        serializer= TickerSerializer(ticker,many=True)
        return Response(serializer.data)
    

    elif request.method =='POST':

        serializer= TickerSerializer(data=request.data)
        df = yf.download(request.data['ticker_name'], period = 'max')
        print(request.data['ticker_name'])
        df = df.reset_index().rename(columns={'index': 'date'})
        # df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        df.to_csv("/Users/lordvoldemort/django_react/second_attempt/frontend/bull_bear/src/data/historicaldata.csv", index=False)
        print(serializer)
        if serializer.is_valid():
            # ticker_name=json.dumps((serializer.validated_data))[1]
            serializer.save()
            # print(request.data['ticker_name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# @api_view(['GET','POST'])
# def TickerDataList(request):
#     if(request.method =='GET'):
#         ticker_data = TickerData.objects.all()
#         serializer = TickerDataSerializer(ticker_data, many = True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # serializer= TickerDataSerializer(data=request.data)
#         print(request.data['searchText'])
#         df = yf.download(request.data['searchText'], period = 'max')
#         print(df)
#         df = df.reset_index().rename(columns={'index': 'date'})
#         df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
#         # df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d')
#         df.rename(columns= {'Adj Close': 'AdjClose'},inplace= True)
#         for i in range(0,len(df)):
#             df['Ticker_name'] = str(request.data['searchText'])
#             df['Date'][i] = df['Date'][i].to_string()
#         stock_data = df.to_dict('records')
#         print(stock_data)

#         # stock_data = json.dumps(stock_data)
#         for i in range (0,len(df)):
#             # data = JSONParser.parse()(stock_data[i])
#             serializer_data = TickerDataSerializer(data = stock_data[i], many = True)
#             print(stock_data[i])
#             if serializer_data.is_valid():
#                 serializer_data.save()
#             else:
#                 continue

#         return Response(serializer_data.data, status=status.HTTP_201_CREATED)
       
        
        
        

# For signup and login             
@api_view(['GET','POST'])
def UserDataList(request):

    if(request.method =='GET'):
        user=UserData.objects.all()
        serializer= UserDataSerializer(user,many=True)
        return Response(serializer.data)
    
    elif (request.method == 'POST'):
        
        user_serializer = UserDataSerializer(data = request.data)
        # user_serializer = json.dumps(user_serializer)
        print(user_serializer)
        if(user_serializer.is_valid()):
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TickerCreate(CreateAPIView):
#     queryset = Ticker.objects.all()
#     serializer_class = TickerSerializer
#     # print(queryset)
    
#     # def list(self):
#     #     # queryset = self.get_queryset()
#     #     # filter = {}
#     #     # serializer = TickerSerializer(queryset, many = True)
#     #     # print (Response(serializer.data))
#     #     data = self.get_object()
#     #     print(data)

#     # list()

        
@api_view(['GET','POST'])
def WatchList(request):
    if(request.method=='GET'):
        stockname = Watchlist.objects.all()
        serializer = WatchlistSerializer(stockname,many = True)
        return Response(serializer.data)
    elif request.method=='POST':
        ticker = request.data['name']
        data = {}
        data.update({"name":ticker})
        df = yf.download(request.data['name'], period= '1d')
        cprice = df['Close'][0]
        data.update({'cprice':cprice})
        watch_serializer = WatchlistSerializer(data=data)
        if watch_serializer.is_valid():
            watch_serializer.save()
            return Response(watch_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(watch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','POST'])
def PriceList(request):
    if(request.method =='GET'):
        stockname = Pricelist.objects.all()
        serializer = PricelistSerializer(stockname,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        ticker = request.data['name']
        data = {}
        data.update({"name":ticker})
        pprice =0
        # df = yf.download(ticker, start="2013-01-01")
        # sdata = df.filter(['Close'])
        # sdataset= sdata.values
        # training_data_len=math.ceil(len(sdataset) * .8)
        # scaler = MinMaxScaler(feature_range=(0,1))
        # scaled_data = scaler.fit_transform(sdataset)
        # train_data = scaled_data[0:training_data_len, :]
        # x_train = []
        # y_train = []
        # for i in range(60, len(train_data)):
        #     x_train.append(train_data[i-60:i, 0])
        #     y_train.append(train_data[i,0])
        # x_train, y_train = np.array(x_train), np.array(y_train)
        # x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
        # #LSTM model
        # # 
        # model = Sequential()
        # model.add(LSTM(100, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        # model.add(LSTM(50,return_sequences=False))
        # model.add(Dense(50))
        # model.add(Dense(1))
        # model.compile(optimizer='adam', loss='mean_squared_error')
        # model.fit(x_train, y_train, batch_size=16, epochs=25)
        # test_data = scaled_data[training_data_len - 60: , :]

        # x_test = []
        # y_test = sdataset[training_data_len:, :]
        # for i in range(60, len(test_data)):
        #     x_test.append(test_data[i-60:i, 0])

        # x_test = np.array(x_test)
        # x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))
        # predictions = model.predict(x_test)
        # predictions = scaler.inverse_transform(predictions)
        # rmse = np.sqrt(np.mean((( predictions - y_test)**2)))
        # data_range=np.max(sdataset)-np.min(sdataset)
        # train = data[:training_data_len]
        # valid = data[training_data_len:]
        # valid['Predictions']=predictions

        # pprice = valid['Predictions'][-1]
        data.update({"pprice":pprice})
        price_serializer = PricelistSerializer(data=data)
        if price_serializer.is_valid():
            price_serializer.save()
            return Response(price_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(price_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


