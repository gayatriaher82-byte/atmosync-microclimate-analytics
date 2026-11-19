
import pandas as pd

# Load Kafka-consumed shipment data
input_file = "data/processed/consumed_shipments.csv"
df = pd.read_csv(input_file)

print("AtmoSync: Kafka Shipment Data Analysis")
print("--------------------------------------")

# Calculate shipment-wise statistics
summary = df.groupby(
    ["shipment_id", "product", "origin", "destination"]
).agg(
    average_temperature=("temperature", "mean"),
    maximum_temperature=("temperature", "max"),
    minimum_temperature=("temperature", "min"),
    average_humidity=("humidity", "mean"),
    maximum_humidity=("humidity", "max"),
    minimum_humidity=("humidity", "min"),
    total_readings=("temperature", "count")
).reset_index()

# Round numerical values
numeric_columns = summary.select_dtypes(
    include="number"
).columns

summary[numeric_columns] = summary[numeric_columns].round(2)

# Display analysis
print("\nShipment Analysis:")
print(summary.to_string(index=False))

# Save analysis results
output_file = "data/processed/kafka_shipment_summary.csv"
summary.to_csv(output_file, index=False)

print("\nAnalysis completed successfully!")
print("Summary saved to:", output_file)
print("Total shipments analysed:", len(summary))
