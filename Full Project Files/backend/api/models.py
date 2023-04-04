from django.db import models


# Create your models here.
class Ticker(models.Model):
    ticker_name=models.CharField(max_length=200)

    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.ticker_name
    
class TickerData(models.Model):
    Ticker_name = models.CharField(max_length=200, default="RELIANCE.NS")
    Date = models.DateField(max_length=200)
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()
    AdjClose = models.FloatField()
    Volume = models.IntegerField()

    def __str__(self):
        return self.Ticker_name
    
class UserData(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    age = models.CharField(max_length=100)
    balance = models.FloatField(default=100000)
    profit = models.FloatField(default=0)
    loss = models.FloatField(default=0)
    qh = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
class LoginData(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__ (self):
        return self.username
    
class Watchlist(models.Model):
    name = models.CharField(max_length=200)
    cprice= models.FloatField()

    def __str__(self):
        return self.name
    
class Pricelist(models.Model):
    name = models.CharField(max_length=200)
    pprice = models.FloatField()

class Newslist(models.Model):
    name = models.CharField(max_length=200)
    sdate = models.DateField()
    edate = models.DateField()

    def __str__(self):
        return self.name

class Buylist(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    q = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name