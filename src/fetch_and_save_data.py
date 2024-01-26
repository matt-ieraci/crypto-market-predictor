import pandas as pd
import requests


def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    print("Status Code:", response.status_code)
    response.raise_for_status()
    return response.json()

def save_data_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    symbols = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT']
    interval = '1d'
    limit = 1000
    for symbol in symbols:
        url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
        test_csv_filename = f'../data/raw/{symbol}_api_data.csv'
        data = fetch_data_from_api(url)
        save_data_to_csv(data, test_csv_filename)

if __name__ == '__main__':
    main()