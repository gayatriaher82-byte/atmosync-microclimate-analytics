
import pandas as pd
import os

# 1. Load original shipment dataset
input_file = "data/raw/shipment_sensor_data.csv"

df = pd.read_csv(input_file)

print("===== ATMOSYNC DATA QUALITY REPORT =====")

# 2. Convert sensor columns to numeric
df["temperature"] = pd.to_numeric(
    df["temperature"], errors="coerce"
)

df["humidity"] = pd.to_numeric(
    df["humidity"], errors="coerce"
)

# 3. Convert timestamp into datetime format
df["timestamp"] = pd.to_datetime(
    df["timestamp"], errors="coerce"
)

# 4. Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# 5. Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# 6. Check invalid humidity readings
invalid_humidity = (
    (df["humidity"] < 0) |
    (df["humidity"] > 100)
)

print("\nINVALID HUMIDITY RECORDS:")
print(invalid_humidity.sum())

# 7. Check invalid timestamps
print("\nINVALID TIMESTAMPS:")
print(df["timestamp"].isna().sum())

# 8. Check invalid temperature values
print("\nMISSING OR NON-NUMERIC TEMPERATURES:")
print(df["temperature"].isna().sum())

# 9. Save processed dataset
output_file = "data/processed/cleaned_shipment_data.csv"

os.makedirs("data/processed", exist_ok=True)

df.to_csv(output_file, index=False)

print("\nPROCESSED DATASET SAVED SUCCESSFULLY!")
print("Output:", output_file)
print("Total records:", len(df))

print("\n===== QUALITY CHECK COMPLETED =====")
