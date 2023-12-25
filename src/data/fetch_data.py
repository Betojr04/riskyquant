import yfinance as yf

# FETCHING THE HISTORICAL STOCK DATA


def fetch_hist_stock_data(ticker, period, selected_columns=None):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)

        if selected_columns is not None:
            selected_columns = [col.strip() for col in selected_columns]
            data = data[selected_columns]

        return data

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# FETCHING CURRENT STOCK DATA


def fetch_curr_stock_data(ticker, selected_columns=None):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        if selected_columns is not None:
            selected_columns = ["Ticker", "Market Cap",
                                "Latest Close", "52-Week High"]

        data = {
            "Ticker": ticker,
            "Market Cap": info.get('marketCap'),
            "Latest Close": info.get('previousClose'),
            "52-Week High": info.get('fiftyTwoWeekHigh')
        }

        if selected_columns is not None:
            data = {key: data[key] for key in selected_columns}

        return data

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
