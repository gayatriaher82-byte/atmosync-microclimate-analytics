
import pandas as pd

# Load shipment sensor data
df = pd.read_csv("data/raw/shipment_sensor_data.csv")
# Convert timestamp column into datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("\nTIMESTAMP DATA TYPE:")
print(df["timestamp"].dtype)

print("\n===== ATMOSYNC DATA ANALYSIS =====")

# 1. Display first five records
print("\n1. FIRST FIVE RECORDS")
print(df.head())

# 2. Dataset size
print("\n2. DATASET SIZE")
print("Rows and columns:", df.shape)

# 3. Dataset information
print("\n3. DATASET INFORMATION")
df.info()

# 4. Check missing values
print("\n4. MISSING VALUES")
print(df.isnull().sum())

# 5. Statistical summary
print("\n5. STATISTICAL SUMMARY")
print(df.describe())

# 6. Average temperature and humidity
print("\n6. AVERAGE CONDITIONS")
print("Average temperature:", round(df["temperature"].mean(), 2))
print("Average humidity:", round(df["humidity"].mean(), 2))

# 7. Shipment-wise temperature analysis
print("\n7. SHIPMENT-WISE AVERAGE TEMPERATURE")
print(df.groupby("shipment_id")["temperature"].mean())

print("\nEDA COMPLETED SUCCESSFULLY!")


# 8. Visualize shipment-wise average temperature
import matplotlib.pyplot as plt

shipment_temp = df.groupby("shipment_id")["temperature"].mean()

plt.figure(figsize=(8, 5))
shipment_temp.plot(kind="bar")

plt.title("Average Temperature by Shipment")
plt.xlabel("Shipment ID")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("reports/shipment_temperature.png")
plt.show()

print("Temperature graph saved successfully!")

