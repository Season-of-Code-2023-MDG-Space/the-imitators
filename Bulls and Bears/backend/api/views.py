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
        ticker = request.data
        print(ticker)