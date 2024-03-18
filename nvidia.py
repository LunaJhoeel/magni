import yfinance as yf
import os

# Create the directory if it doesn't exist
data_directory = 'data/raw'
os.makedirs(data_directory, exist_ok=True)

# Ticker symbol for NVIDIA
ticker_symbol = "NVDA"

# Fetching data for NVIDIA stock
nvidia = yf.Ticker(ticker_symbol)

# Fetching historical data for daily opening prices
historical_data = nvidia.history(period="max")

# Selecting only the 'Open' column
opening_prices = historical_data['Open']

# Saving the opening prices to a CSV file
csv_file_path = os.path.join(data_directory, 'opening_prices.csv')
opening_prices.to_csv(csv_file_path, header=True)

print(f"Opening prices saved to {csv_file_path}")
