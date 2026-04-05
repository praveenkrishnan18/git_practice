import csv

def extract_data(filepath="data/raw_sales.csv"):
    """Read raw CSV and return list of dicts."""
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    print(f"[EXTRACT] Loaded {len(data)} records from {filepath}")
    return data

if __name__ == "__main__":
    rows = extract_data()
    print(f"Sample row: {rows[0]}")