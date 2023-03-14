import sqlite3
import yfinance as yf
from datetime import datetime
import pytz

# conn = sqlite3.connect('bullbears.db')

# c = conn.cursor()

# Creating Parent Table
# c.execute(''' CREATE TABLE users(
#         Username TEXT,
#         Name TEXT,
#         Age INTEGER,
#         Password TEXT,
#         Balance REAL,
#         Stock Quantity Holding INTEGER,
#         Profit REAL,
#         Loss REAL,
#         PRIMARY KEY (Username)
#         );
# ''')

# Creating Child Table
# c.execute(''' CREATE TABLE stock(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Username TEXT,
#         Stock_Name TEXT,
#         Quantity_Holding INTEGER,
#         Purchased_Price REAL,
#         Sold_Price REAL,
#         Purchasing_Date TEXT,
#         Selling_Date TEXT,
#         FOREIGN KEY (Username) REFERENCES users(Username)
#         );
# ''')

# To display all user table
conn=sqlite3.connect('bullbears.db')
c= conn.cursor()
c.execute("SELECT * FROM users")
items = c.fetchall()
for item in items:
    print(item)
conn.commit()
conn.close()


#
# # To display the data of username table
# def show_user(username):
#     conn= sqlite3.connect('bullbears.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM users WHERE Username= (?)",username)
#     items= c.fetchall()
#     for item in items:
#         print(item)
#     conn.commit()
#     conn.close()
#
# # To add the data in username table
# def add_one_user(username,name,age,password,balance,sqn,prof,loss):
#     conn= sqlite3.connect('bullbears.db')
#     c = conn.cursor()
#     c.execute('''INSERT INTO users VALUES (?,?,?,?,?,?,?,?)''',
#               (username,name,age,password,balance,sqn,prof,loss)
#               )
#     conn.commit()
#     conn.close()
#
# # To add the data in stocks table
# def add_one_stock(username,name,qnh,purchprice,soldprice,pdate,sdate):
#     conn= sqlite3.connect('bullbears.db')
#     c = conn.cursor()
#     c.execute('''INSERT INTO stock VALUES (?,?,?,?,?,?,?)''',
#               (username,name,qnh,purchprice,soldprice,pdate,sdate)
#               )
#     conn.commit()
#     conn.close()
#
# # To display the data of stocks table
# def show_stock(username):
#     conn= sqlite3.connect('bullbears.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM stock WHERE Username= (?)",username)
#     items= c.fetchall()
#     for item in items:
#         print(item)
#     conn.commit()
#     conn.close()
#
#
# # To update the balance of user
# def update_bal(username,bal):
#     conn=sqlite3.connect('bullbears.db')
#     c= conn.cursor()
#     c.execute('''UPDATE users SET Balance=(?) WHERE Username=(?)
#     ''',(bal,username))
#
#     conn.commit()
#     conn.close()
#
# def show_bal(username):
#     conn= sqlite3.connect('bullbears.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM users WHERE Username= (?)",username)
#     items= c.fetchall()
#     return items[4]
#     conn.commit()
#     conn.close()
#
# username=input("Enter your username")
# name=input("Enter your Full Name")
# age=input("Enter your age")
# password=input("Enter your password")
# balance=100000
# # print("Your Preloaded balance is "+ str(balance))
# sqn=0
# # print("Your Stocks Quantity is "+ str(sqn))
# prof=0
# # print("Your Profit is "+ str(prof))
# loss=0
# # print("Your Loss is "+ str(loss))
#
# print("1-Add your user info")
# print("2-Display your User Info")
# print("3-Display your Stock Info")
# print("4-Buy Stock")
# print("5-Sell Stock")
# print("Enter Choice")
# ch=input()
#
# if(ch==1):
#     add_one_user(username,name,age,password,balance,sqn,prof,loss)
# elif(ch==2):
#     show_user(username)
# elif(ch==3):
#     show_stock(username)
# elif(ch==4):
#     sname=input("Enter the ticker for that stock name")
#     qnhold=input("Enter the quantity of that stock")
#     df=yf.download(sname,start=datetime.now())
#     purprice=df['Close'].value
#     current_date = datetime.now(pytz.timezone('Asia/Kolkata'))
#     date_time = current_date.strftime("%m/%d/%Y, %H:%M:%S")
#     pdate=date_time
#     sprice=0
#     sdate=0
#     add_one_stock(username,sname,qnhold,purprice,sprice,pdate,sdate)
#     bought= purprice*qnhold
#     bal=show_bal()
#
#     update_bal(username,bal-bought)
# elif(ch==5):
#     sname=input("Enter the ticker for that stock name")
#     qnhold=input("Enter the quantity of that stock")
#     df=yf.download(sname,start=datetime.now())
#     sprice=df['Close'].value
#     current_date = datetime.now(pytz.timezone('Asia/Kolkata'))
#     date_time = current_date.strftime("%m/%d/%Y, %H:%M:%S")
#     sdate=date_time
#     purprice=0
#     pdate=0
#     add_one_stock(username,sname,qnhold,purprice,sprice,pdate,sdate)
#     bought= sprice*qnhold
#     bal=show_bal()
#
#     update_bal(username,bal+bought)



