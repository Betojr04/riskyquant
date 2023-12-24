import yfinance as yf


def fetch_stock_data(ticker):
    data = yf.Ticker(ticker)
    return data.history(period="1y")
