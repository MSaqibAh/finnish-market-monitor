# 🌐 Data Sources – Finnish Market Monitor

This project integrates **publicly available open data APIs** from Finland’s main financial and statistical institutions.

---

## 1️⃣ Stock Market Data
**Source:** [Yahoo Finance](https://finance.yahoo.com/)  
**Method:** `yfinance` Python package  
**Tickers Used:**
- NOKIA.HE (Nokia Corporation)
- FORTUM.HE (Fortum Oyj)
- KNEBV.HE (Kone Oyj)
- NESTE.HE (Neste Corporation)
- OUT1V.HE (Outokumpu Oyj)

**Data Collected:**
- Open, High, Low, Close (OHLC)
- Volume
- Adjusted Close
- Frequency: Daily

**Usage:**
Stored in `raw.stock_prices` table.

---

## IN PROGRESS

## 2️⃣ Interest Rate Data
**Source:** [Bank of Finland – Open Data](https://www.suomenpankki.fi/en/Statistics/open-data/)  
**Dataset:** Euribor 3-month rate, ECB deposit and refinancing rates  
**Format:** JSON / CSV API endpoint  
**Usage:**  
- Stored in `raw.interest_rates`  
- Used to analyze correlation between rates and equity returns.

---

## 3️⃣ Macroeconomic Indicators
**Source:** [Statistics Finland API](https://www.stat.fi/en/statistics/luettelo)  
**Indicators:**
- CPI (Consumer Price Index)
- Industrial Production Index
- GDP growth

**Usage:**
- Stored in `raw.macro_indicators`
- Combined with stock & rate data in `model.market_summary`

---

## 🔗 Update Frequency
| Source | Refresh | Method |
|--------|----------|--------|
| Yahoo Finance | Daily | Python (yfinance) |
| Bank of Finland | Daily | Python (requests + CSV API) |
| Statistics Finland | Monthly | Python (requests + JSON API) |

---

## 🧩 Integration Notes
All data sources are harmonized on the **`ts_date`** field for joining across domains.  
Missing dates are forward-filled in SQL to ensure smooth visualization in Power BI.

---

📄 **Author:** Muhammad Saqib Chouhdry
