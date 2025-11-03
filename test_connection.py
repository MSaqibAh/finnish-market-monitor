from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:password@localhost:5432/market_monitor")

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'Connection successful!'"))
        print(result.scalar())
except Exception as e:
    print("❌ Error:", e)
