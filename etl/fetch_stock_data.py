import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine("postgresql://postgres:password@localhost:5432/market_monitor")

# Step 1: Choose which stocks to fetch
tickers = ["NOKIA.HE", "FORTUM.HE", "NESTE.HE", "KNEBV.HE", "OUT1V.HE"]

# Step 2: Download stock data using yfinance
print("📈 Fetching stock data from Yahoo Finance...")
data = yf.download(tickers, start="2020-01-01", group_by="ticker")


# Step 3: Reshape and clean the data
frames = []

for ticker in tickers:
    df = data[ticker].reset_index()
    df["ticker"] = ticker
    df = df.rename(columns={
        "Date": "ts_date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume"
    })
    frames.append(df)

all_data = pd.concat(frames)
print(f"✅ Downloaded {len(all_data)} rows in total.")

# Step 4: Store the data in PostgreSQL

all_data.to_sql("stock_prices", engine, schema="raw", if_exists="replace", index=False)
print("💾 Data saved to database: raw.stock_prices")

# Step 5: Show a small preview

print(all_data.head())
