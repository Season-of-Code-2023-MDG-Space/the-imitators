from django.urls import path, include
from . import views

urlpatterns = [
    path('ticker/', views.TickerList),
    # path('ticker/', views.TickerList().as_view()),
    # path('ticker/create/', views.TickerCreate.as_view()),
    # path('tickerdata/', views.TickerDataList),
    path('userdata/', views.UserDataList),

    ]