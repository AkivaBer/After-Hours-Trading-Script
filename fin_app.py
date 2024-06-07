import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define the function to fetch and process the stock data
def fetch_and_process_stock_data(ticker, from_date, to_date, api_key):
    url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/minute/{from_date}/{to_date}?adjusted=true&sort=asc&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if data.get('status') != 'OK':
        raise ValueError("Error fetching data from API")

    results = data['results']
    processed_data = []

    for result in results:
        processed_data.append({
            "timestamp": datetime.fromtimestamp(result['t'] / 1000),
            "open": result['o'],
            "high": result['h'],
            "low": result['l'],
            "close": result['c'],
            "volume": result['v']
        })

    return processed_data

def get_date_from_user():
    while True:
        user_input = input("Please enter a date (YYYY-MM-DD): ")
        try:
            # Try to parse the date to ensure it's in the correct format
            date = datetime.strptime(user_input, '%Y-%m-%d')
            # If parsing is successful, return the formatted date
            return date.strftime('%Y-%m-%d')
        except ValueError:
            # If the input is not in the correct format, inform the user and ask again
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

# Define the function to plot the data
def plot_stock_data(processed_data, ticker):
    df = pd.DataFrame(processed_data)
    df.set_index('timestamp', inplace=True)

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['close'], marker='o')
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.title(f'{ticker} After Hours Close Prices')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to the current directory
    plot_filename = f'{ticker}_after_hours.png'
    plt.savefig(plot_filename)
    plt.close()

    print(f'Plot saved as {plot_filename}')

# Define the function to save the data to a CSV file
def save_to_csv(processed_data, filename):
    df = pd.DataFrame(processed_data)
    df.to_csv(filename, index=False)
    print(f'Data saved to {filename}')

# Main script execution
if __name__ == '__main__':
    ticker = input("What ticker do you want? ")
    print("You will not be prompted for two dates. The first is the 'from date' where you want the data to begin and the second is the 'to date'")
    from_date = get_date_from_user()
    to_date = get_date_from_user()

    api_key = 'cU7iAyGm2zowqXsRrvoo9UXwUciqo98k'
    
    processed_data = fetch_and_process_stock_data(ticker, from_date, to_date, api_key)
    plot_stock_data(processed_data, ticker)
    save_to_csv(processed_data, f'{ticker}_after_hours_{from_date}.csv')