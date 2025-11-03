from sqlalchemy import create_engine, text

# ------------------------------------------------------
# Replace 'YOUR_PASSWORD' with your actual PostgreSQL password.
# Example: "postgresql://postgres:mysecret123@localhost/market_monitor"
# ------------------------------------------------------

engine = create_engine("postgresql://postgres:password@localhost:5432/market_monitor")

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'Connection successful!'"))
        print(result.scalar())
except Exception as e:
    print("❌ Error:", e)
