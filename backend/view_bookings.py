import sqlite3
from pathlib import Path

# Database ko backend folder mein dhundhega
db_path = Path(__file__).resolve().parent / "bookings.db"

conn = sqlite3.connect(db_path)

# Database ki saari tables aur records dikhao
tables = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

for (table,) in tables:
    if table.startswith("sqlite_"):
        continue

    print(f"\nTABLE: {table}")

    for row in conn.execute(f'SELECT * FROM "{table}"'):
        print(row)

conn.close()