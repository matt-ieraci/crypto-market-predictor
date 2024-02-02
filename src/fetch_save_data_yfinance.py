import yfinance as yf

def fetch_data(ticker, start_date='2020-01-01', end_date=None):
    """
    Fetch historical market data for a given ticker from Yahoo Finance.
    
    :param ticker: The ticker symbol for the asset (e.g., 'BTC-USD').
    :param start_date: The start date for the data (format: 'YYYY-MM-DD').
    :param end_date: The end date for the data (format: 'YYYY-MM-DD').
    :return: A pandas DataFrame containing the historical market data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    
    return data