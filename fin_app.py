import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
from flask import Flask, request, render_template, send_file
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stock = request.form['stock']
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=1min&apikey=WI5ULB4FHQTI3WM0'
        r = requests.get(url)
        data = r.json()

        if "Time Series (1min)" in data:
            time_series = data["Time Series (1min)"]

            timestamps = []
            close_prices = []

            for timestamp, values in time_series.items():
                timestamps.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
                close_prices.append(float(values["4. close"]))

            timestamps, close_prices = zip(*sorted(zip(timestamps, close_prices)))

            # Plotting the data
            plt.figure(figsize=(12, 6))
            plt.plot(timestamps, close_prices, marker='o')
            plt.xlabel('Time')
            plt.ylabel('Close Price')
            plt.title(f'{stock} After Hours Close Prices')
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Save the plot to a BytesIO object
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plt.close()

            return send_file(img, mimetype='image/png')
        else:
            error_message = data.get("Error Message", "Invalid API call.")
            return render_template('index.html', error=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
