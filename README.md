# BULLS & BEARS

Contents
- Setup
- Database
- What is Bulls and Bears?
- How to use our web app?
   i) Sign Up/ Login page
   ii) Dashboard
   iii) Watchlist
   iv)
- Future Scopes
- Contributors

# Setup
Clone the Repository and then in the project directory run the CLI command  python manage.py runserver

## Languages/Framework and their version

Django 4.1.7

html5lib 1.1

keras 2.12.0

python-dateutil 2.8.2

yfinance 0.2.14

# Database
We have imported our database from the API yahoo finance, trading view , quandle.

# What is Bulls and Bears?
<img width="360" alt="Screenshot 2023-03-27 at 23 01 29" src="https://user-images.githubusercontent.com/95199085/228024023-1f36f450-b0fa-4880-92b3-327454f87997.png">
It is a stock market simulation web page that can provide access to real-time market data, helping traders to make informed decisions. Also, traders lack knowledge about the stock market and its various aspects, such as market trends and dynamics.
Simulation can help traders to learn and test and perfect their timing of trades, reducing the risk of loss due to poor timing.
This web application will provide a common platform to display historical data, real-time market images, videos and articles to give basic knowledge to people.

# How to use our web app?
## i) Sign Up/ Log in page
<img width="360" alt="Screenshot 2023-03-27 at 23 01 41" src="https://user-images.githubusercontent.com/95199085/228023828-54e0b761-4a34-4cb8-94c4-356fcb7c6f44.png">

To go through our web page one needs to enter his/her details in the sign in page.
## ii) Dashboard
<img width="360" alt="Screenshot 2023-03-27 at 23 01 35" src="https://user-images.githubusercontent.com/95199085/228024211-b4f21722-39a3-49a7-a6fd-eb931a153c25.png">

Submit the ticker name for the stock whose closing price will be displayed.eg- 'AAPL', 'ADANIENT'..
## iii) Watchlist
<img width="360" alt="Screenshot 2023-03-27 at 23 42 47" src="https://user-images.githubusercontent.com/95199085/228130868-9157de66-1e2d-472d-8767-78ae9a42d94d.png">  <img width="360" alt="Screenshot 2023-03-27 at 22 51 53" src="https://user-images.githubusercontent.com/95199085/228024575-24104248-b134-439f-ba17-a7048a4c85a6.png">
<img width="360" alt="Screenshot 2023-03-27 at 23 02 01" src="https://user-images.githubusercontent.com/95199085/228024503-550ef050-3443-48ea-9667-f999cee75d88.png">
<img width="360" alt="Screenshot 2023-03-27 at 23 43 16" src="https://user-images.githubusercontent.com/95199085/228130900-21817042-a536-4f35-a7e4-297f59a47153.png">

The searched stock gets appended in the backend server and this provides the real time trading data and analysis curve (in the form of candle sticks) of the present stock at the user end.

![Image 28-03-23 at 01 08](https://user-images.githubusercontent.com/95199085/228130975-c8344213-b322-4957-90c2-08c0a8422224.jpg)

## iv) 
# Future Scope
Till now , we have used LSTM model in our ML model. We also used RandomForests as they are more used widely for larger datsets, but due to its lack of inaccuracies and exclusivity for different types of datasets. RandomForests are more feasible as they predict whether the closing price will fall or rise, the next day.
Also a chatbot feature was used, but due to depreciated libraries of neuralnine, the intents file could not be imported.
# Contributors
[Yathartha Rana](https://github.com/YatharthaRana)

[Sumit Raj](https://github.com/sumit65151)

[Vaibhav Nandan](https://github.com/Vaibnandan)



