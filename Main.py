import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical stock data for SPY (S&P 500) for the last 2 years
ticker = "SPY"
start_date = "2022-01-01"
end_date = "2024-01-01"
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate moving averages
data['10D_MA'] = data['Adj Close'].rolling(window=10).mean()
data['30D_MA'] = data['Adj Close'].rolling(window=30).mean()
data['10W_MA'] = data['Adj Close'].rolling(window=10*5).mean()  # Assuming 5 trading days per week
data['30W_MA'] = data['Adj Close'].rolling(window=30*5).mean()

# Plot the data and moving averages
plt.figure(figsize=(10, 6))
plt.plot(data['Adj Close'], label='Adjusted Close')
plt.plot(data['10D_MA'], label='10-day MA')
plt.plot(data['30D_MA'], label='30-day MA')
plt.plot(data['10W_MA'], label='10-week MA')
plt.plot(data['30W_MA'], label='30-week MA')

plt.title(f"{ticker} Stock Price and Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
