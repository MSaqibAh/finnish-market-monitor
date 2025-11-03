-- ===============================================
-- Market Overview Model
-- Summarizes stock performance and volatility
-- ===============================================

DROP TABLE IF EXISTS model.market_overview;

CREATE TABLE model.market_overview AS
WITH daily_returns AS (
    SELECT
        ticker,
        ts_date,
        close,
        LAG(close) OVER (PARTITION BY ticker ORDER BY ts_date) AS prev_close,
        volume
    FROM raw.stock_prices
)
SELECT
    ticker,
    COUNT(*) AS trading_days,
    ROUND(AVG(close)::numeric, 2) AS avg_close,
    ROUND((SUM(volume) / 1e6)::numeric, 2) AS total_volume_millions,
    ROUND(((MAX(close) - MIN(close)) / NULLIF(MIN(close), 0) * 100)::numeric, 2) AS price_change_pct,
    ROUND((STDDEV((close - prev_close) / NULLIF(prev_close, 0)) * 100)::numeric, 2) AS volatility_pct
FROM daily_returns
WHERE prev_close IS NOT NULL
GROUP BY ticker
ORDER BY ticker;
