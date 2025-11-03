# 💹 Finnish Market Monitor – Data Analytics Project

**Author:** Muhammad Saqib Chouhdry  
**Date:** November 2025

---

## 🎯 Project Overview

This project builds an end-to-end **data analytics pipeline** for tracking the Finnish stock market and exploring how **interest rates** and **macroeconomic indicators** affect equity performance.

It demonstrates real-world skills in **ETL, SQL modeling, visualization**, and **insight generation**.

---

## 🏗️ Architecture

```

APIs / Open Data
↓
Python (ETL scripts: fetch_stock_data.py, fetch_interest_rates.py)
↓
PostgreSQL (Schemas: raw, model)
↓
SQL Models (market_overview, market_summary)
↓
Power BI Dashboard

```

**Stack:**  
Python • PostgreSQL • Power BI • SQLAlchemy • yfinance • pandas • matplotlib

---

## ✅ Current Progress

| Component                | Description                                                               | Status         |
| ------------------------ | ------------------------------------------------------------------------- | -------------- |
| **Database Setup**       | PostgreSQL database with `raw` + `model` schemas                          | ✅             |
| **Stock ETL**            | Yahoo Finance data (NOKIA HE, FORTUM HE, NESTE HE …) → `raw.stock_prices` | ✅             |
| **SQL Modeling**         | `model.market_overview` – avg price, volatility, volume                   | ✅             |
| **Power BI Dashboard**   | KPI cards + price & volatility visuals                                    | ✅             |
| **Interest Rate ETL**    | Bank of Finland API (Euribor 3M etc.)                                     | ⚙️ In progress |
| **Macro ETL**            | Statistics Finland API (CPI, GDP, Industrial Index)                       | ⚙️ Planned     |
| **Market Summary Model** | Combine stock + rate + macro                                              | ⚙️ Planned     |
| **Automation**           | Daily Python refresh / Task Scheduler                                     | ⚙️ Planned     |

---

## 🧮 Example: Python ETL

```python
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:YOUR_PASSWORD@localhost:5432/market_monitor")

tickers = ["NOKIA.HE", "FORTUM.HE", "NESTE.HE"]
data = yf.download(tickers, start="2020-01-01").stack(level=1).reset_index()
data.columns = ["ts_date","ticker","open","high","low","close","adj_close","volume"]
data.to_sql("stock_prices", engine, schema="raw", if_exists="append", index=False)

print("✅ Stock data loaded successfully.")
```

---

## 🗃️ Example: SQL Model

```sql
DROP TABLE IF EXISTS model.market_overview;

CREATE TABLE model.market_overview AS
SELECT
    ticker,
    ROUND(AVG(close)::numeric,2) AS avg_close,
    ROUND(STDDEV(close)::numeric,2) AS volatility,
    ROUND((MAX(close)-MIN(close))/NULLIF(MIN(close),0)*100,2) AS price_change_pct,
    ROUND(SUM(volume)/1000000.0,2) AS total_volume_millions
FROM raw.stock_prices
GROUP BY ticker;
```

---

## 📊 Power BI Dashboard

- **KPI Cards:** Top Gainer | Top Loser | Most Volatile | Highest Volume
- **Charts:** Avg Close / Volatility trends per ticker
- _(Planned)_ Overlay Euribor and CPI

---

## 🧠 Key Learnings

- Designed a full **Python → PostgreSQL → Power BI** pipeline.
- Built reproducible **SQL models** for financial analysis.
- Focused on **decision-support insights** – not just visuals.

---

## 📂 Project Structure

```
finnish-market-monitor/
├── etl/
│   ├── fetch_stock_data.py
│   ├── fetch_interest_rates.py
│   └── fetch_macro_data.py
├── sql/
│   ├── model_market_overview.sql
│   └── model_market_summary.sql
├── notebooks/
│   ├── analysis.ipynb
│   └── visualize_stock_data.py
├── images/
├── docs/
│   ├── project_summary.pdf
│   ├── architecture.txt
│   └── data_sources.md
├── README.md
├── requirements.txt
└── test_connection.py
```

---

## 🧩 Next Steps

1. Integrate Bank of Finland (Euribor 3M / ECB rates).
2. Add Statistics Finland macroeconomic data.
3. Create `model.market_summary` to combine all sources.
4. Automate daily refresh and publish Power BI dashboard.

---

## 🧠 Skills Showcased

| Area                 | Tools / Concepts                                    |
| -------------------- | --------------------------------------------------- |
| **Data Engineering** | PostgreSQL, SQL modeling                            |
| **ETL Automation**   | Python, pandas, SQLAlchemy, APIs                    |
| **Analytics & BI**   | Power BI, DAX KPIs, visual storytelling             |
| **Finance Domain**   | Volatility, interest-rate impact, sector comparison |

---

## 🚀 Impact

This project demonstrates how an analyst can build a **scalable, insight-driven financial analytics system**.

It helps management identify:

- Market stress via volatility
- Rate-sensitive sectors
- Data-based investment opportunities
