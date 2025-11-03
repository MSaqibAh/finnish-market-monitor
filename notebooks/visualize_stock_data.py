import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


# Connect to your PostgreSQL database
engine = create_engine("postgresql://postgres:password@localhost:5432/market_monitor")


# Step 1: Load Nokia data from the database
query = """
SELECT ts_date, close
FROM raw.stock_prices
WHERE ticker = 'NOKIA.HE'
ORDER BY ts_date;
"""

df = pd.read_sql(query, engine)

print(f"✅ Loaded {len(df)} rows for NOKIA.HE")
print(df.head())

# Step 2: Plot the trend
plt.figure(figsize=(10, 5))
plt.plot(df["ts_date"], df["close"], color="royalblue", linewidth=1.5)
plt.title("📈 Nokia Stock Price Trend (2020–Present)")
plt.xlabel("Date")
plt.ylabel("Close Price (€)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show(block=True)

# Show daily % change
df["pct_change"] = df["close"].pct_change() * 100  # percentage difference from previous day
df = df.dropna(subset=["pct_change"])

plt.figure(figsize=(10, 5))
plt.plot(df["ts_date"], df["pct_change"], color="orange", linewidth=1)
plt.title("📊 Nokia Daily % Change")
plt.xlabel("Date")
plt.ylabel("Percent Change (%)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show(block=True)
