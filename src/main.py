from data.fetch_data import fetch_hist_stock_data, fetch_curr_stock_data
from analysis.var import calculate_var, calculate_daily_returns


def main():
    # asking user for input of what ticker symbol to retrieve data for
    ticker = input("Enter a ticker symbol (example: 'MSFT'): ")
    # asking for the data user wants retreived
    data_type = input(
        "Enter the type of data you want (e.g historical, current)")
    data = None

    # if-elif statement to handle the different responses and error messages
    if data_type.lower() == 'historical':
        period = input("Enter the period for historical data (e.g 1mo, 1y): ")
        historical_data = fetch_hist_stock_data(ticker, period)
        daily_returns = calculate_daily_returns(historical_data)

        if daily_returns is not None:
            var = calculate_var(daily_returns, confidence_level=0.95)
            print(f"1-day 95% VaR: {var}")
        else:
            print("Unable to print daily returns.")

    elif data_type.lower() == 'current':
        data = fetch_curr_stock_data(ticker)
        if data is not None:
            print(data)
        else:
            print("Unable to fetch current data.")
    else:
        print("Invalid data type selection")


if __name__ == "__main__":
    main()
