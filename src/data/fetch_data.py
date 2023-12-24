import yfinance as yf

# FETCHING THE HISTORICAL STOCK DATA


def fetch_hist_stock_data(ticker, period):
    try:
        stock = yf.Ticker(ticker)
        return stock.history(period=period)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# FETCHING CURRENT STOCK DATA


def fetch_curr_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        latest_close = info.get('previousClose')
        fifty_two_week_high = info.get('fiftyTwoWeekHigh')
        market_cap = info.get('marketCap')

        return {
            "Ticker": ticker,
            "Latest Close": latest_close,
            "52-Week High": fifty_two_week_high,
            "Market Cap": market_cap
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
