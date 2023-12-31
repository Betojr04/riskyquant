from data.fetch_data import fetch_hist_stock_data, fetch_curr_stock_data
from analysis.var import calculate_var, calculate_daily_returns, calculate_cvar, enhanced_backtest_var


def main():
    # asking user for input of what ticker symbol to retrieve data for
    ticker = input("Enter a ticker symbol (example: 'MSFT'):")
    # asking for the data user wants retrieved
    data_type = input(
        "Enter the type of data you want (e.g., historical, current):")
        

    # for historical data selection
    if data_type.lower() == 'historical':
        period = input("Enter the period for historical data (e.g., 1mo, 1y):")
        selected_columns = ["Close"]  # Close is needed for VaR and backtesting
        historical_data = fetch_hist_stock_data(
            ticker, period, selected_columns)

        if historical_data is not None:
            print("\nHistorical Data:")
            print(historical_data.head())

            daily_returns = calculate_daily_returns(historical_data)
            if daily_returns is not None:
                var = calculate_var(daily_returns, confidence_level=0.95)
                print(f"\n1-day 95% VaR: {var}")

                # Enhanced backtesting
                exceedance_rate, var_values = enhanced_backtest_var(
                    historical_data, confidence_level=0.95)
                print(
                    f"Enhanced backtesting exceedance rate: {exceedance_rate:.2%}")

                cvar = calculate_cvar(daily_returns, var,
                                      confidence_level=0.95)
                print(f"1-day 95% CVaR: {cvar}")
            else:
                print("Unable to calculate daily returns.")
        else:
            print("Unable to fetch historical data.")

    # for current data selection
    elif data_type.lower() == 'current':
        current_data = fetch_curr_stock_data(ticker)
        if current_data is not None:
            print("\nCurrent Data:")
            print(current_data)
        else:
            print("Unable to fetch current data.")
    else:
        print("Invalid data type selection")


if __name__ == "__main__":
    main()
