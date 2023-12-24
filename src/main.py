from fetch_data import *


def main():
    ticker = input("Enter a ticker symbol (example: 'MSFT'): ")
    stock_data = fetch_stock_data(ticker)
    print(stock_data)


if __name__ == "__main__":
    main()
