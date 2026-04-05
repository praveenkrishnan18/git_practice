import csv, os

def load(data, filepath="output/clean_sales.csv"):
    """Save transformed data to output CSV."""
    os.makedirs("output", exist_ok=True)

    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"[LOAD] Saved {len(data)} records to {filepath}")

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    raw   = extract()
    clean = transform(raw)
    load(clean)