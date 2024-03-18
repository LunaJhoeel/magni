import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from chronos import ChronosPipeline

# Load the filled DataFrame
csv_file_path = 'data/processed/opening_prices_filled.csv'
opening_prices_filled = pd.read_csv(csv_file_path, index_col=0, parse_dates=True)

# Convert DataFrame to torch tensor
context = torch.tensor(opening_prices_filled['Open'].values, dtype=torch.float32)

# Define the prediction length
prediction_length = 30  # Change this to your desired prediction length

# Load the Chronos model
pipeline = ChronosPipeline.from_pretrained(
    "amazon/chronos-t5-large",
    device_map="cuda",
    torch_dtype=torch.bfloat16,
)

# Make predictions
forecast = pipeline.predict(context, prediction_length)  # shape [num_series, num_samples, prediction_length]

# Generate forecast dates
forecast_index = pd.date_range(start=opening_prices_filled.index[-1], periods=prediction_length+1)[1:]
low, median, high = np.quantile(forecast[0].numpy(), [0.1, 0.5, 0.9], axis=0)

# Create a DataFrame for the forecast
forecast_df = pd.DataFrame({'Date': forecast_index, 'Low': low, 'Median': median, 'High': high})
forecast_df.set_index('Date', inplace=True)

# Save the forecast to a CSV file
forecast_csv_path = 'data/forecast/forecast_next_30_days.csv'
forecast_df.to_csv(forecast_csv_path)

# Visualization
plt.figure(figsize=(8, 4))
plt.plot(opening_prices_filled.index, opening_prices_filled['Open'], color="royalblue", label="historical data")
plt.plot(forecast_index, median, color="tomato", label="median forecast")
plt.fill_between(forecast_index, low, high, color="tomato", alpha=0.3, label="80% prediction interval")
plt.legend()
plt.grid()
plt.savefig('figures/forecast_nvidia.png')
