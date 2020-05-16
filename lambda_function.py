import yfinance as yf


# this is just a test implementation
def lambda_handler(event, context):
    tickers = yf.Tickers('msft aapl goog')
    print(tickers.tickers.MSFT.history())

if __name__ == "__main__":
    # again, this is to test locally
    lambda_handler({}, {})
