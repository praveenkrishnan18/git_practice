import csv, random, os
from datetime import datetime, timedelta

os.makedirs("data", exist_ok=True)

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
regions  = ["North", "South", "East", "West"]

rows = []
base = datetime(2024, 1, 1)
for i in range(20):
    rows.append({
        "order_id":   f"ORD{1000+i}",
        "product":    random.choice(products),
        "quantity":   random.randint(1, 10),
        "price":      round(random.uniform(10, 500), 2),
        "region":     random.choice(regions),
        "order_date": (base + timedelta(days=i)).strftime("%Y-%m-%d"),
        "status":     random.choice(["completed", "pending", "NULL"])
    })

with open("data/raw_sales.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Raw data created: data/raw_sales.csv")