from django.urls import path, include
from . import views

urlpatterns = [
    path('ticker/', views.TickerList),
    # path('ticker/', views.TickerList().as_view()),
    # path('ticker/create/', views.TickerCreate.as_view()),
    # path('tickerdata/', views.TickerDataList),
    path('userdata/', views.UserDataList),
    path('watchlist/',views.WatchList),
    path('prediction/',views.PriceList),
    path('login/',views.LoginList),
    # path('portfolio/',views.PortfolioList),
    path('news/',views.NewsList),
    path('buy/',views.BuyList),
    path('portfoliodata/',views.PorfolioDataList),
    path('stockcard/',views.StockList),


    ]