def transform(data):
    """Clean and enrich the raw data."""
    cleaned = []
    skipped = 0

    for row in data:
        # 1. Skip rows with NULL status
        if row["status"] == "NULL":
            skipped += 1
            continue

        # 2. Cast types
        row["quantity"] = int(row["quantity"])
        row["price"]    = float(row["price"])

        # 3. Add derived column: total_revenue
        row["total_revenue"] = round(row["quantity"] * row["price"], 2)

        # 4. Normalize region to uppercase
        row["region"] = row["region"].upper()

        cleaned.append(row)

    print(f"[TRANSFORM] {len(cleaned)} records cleaned, {skipped} skipped (NULL status)")
    return cleaned

if __name__ == "__main__":
    from extract import extract
    raw  = extract()
    clean = transform(raw)
    print(f"Sample transformed row: {clean[0]}")