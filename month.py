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
prediction_length = 30  # Desired prediction length

# Load the Chronos model
pipeline = ChronosPipeline.from_pretrained(
    "amazon/chronos-t5-small",
    device_map="cuda",
    torch_dtype=torch.bfloat16,
)

# Make predictions
forecast = pipeline.predict(context, prediction_length)

# Visualize the forecast
forecast_index = pd.date_range(start=opening_prices_filled.index[-1], periods=prediction_length+1)[1:]
low, median, high = np.quantile(forecast[0].numpy(), [0.1, 0.5, 0.9], axis=0)

# Filter the last 3 months of historical data for plotting
three_months_ago = opening_prices_filled.index[-1] - pd.DateOffset(months=3)
filtered_opening_prices = opening_prices_filled[opening_prices_filled.index >= three_months_ago]

plt.figure(figsize=(8, 4))
plt.plot(filtered_opening_prices.index, filtered_opening_prices['Open'], color="royalblue", label="historical data (last 3 months)")
plt.plot(forecast_index, median, color="tomato", label="median forecast")
plt.fill_between(forecast_index, low, high, color="tomato", alpha=0.3, label="80% prediction interval")
plt.legend()
plt.grid()
plt.savefig('figures/forecast_nvidia_last_3_months.png')
