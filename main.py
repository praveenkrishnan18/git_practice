from extract   import extract_data
from transform import transform
from load      import load

def run_pipeline():
    print("=" * 40)
    print("  SALES DATA PIPELINE - STARTING")
    print("=" * 40)
    raw   = extract_data()
    clean = transform(raw)
    load(clean)
    print("=" * 40)
    print("  PIPELINE COMPLETE ✅")
    print("=" * 40)

if __name__ == "__main__":
    run_pipeline()