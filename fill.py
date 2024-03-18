import pandas as pd

# Load the CSV file containing opening prices
csv_file_path = 'data/raw/opening_prices.csv'
opening_prices = pd.read_csv(csv_file_path, index_col=0, parse_dates=True)

# Forward fill missing values
opening_prices_filled = opening_prices.ffill()

# Save the updated data back to the CSV file
updated_csv_file_path = 'data/processed/opening_prices_filled.csv'
opening_prices_filled.to_csv(updated_csv_file_path)

print(f"Forward-filled opening prices saved to {updated_csv_file_path}")
