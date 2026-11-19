
import pandas as pd

# Load shipment sensor data
input_file = "data/processed/consumed_shipments.csv"
df = pd.read_csv(input_file)

print("AtmoSync: Shipment Temperature Risk Analysis")
print("--------------------------------------------")

# Define initial project temperature thresholds
def classify_risk(temperature):
    if temperature > 12:
        return "High Risk"
    elif temperature > 8:
        return "Moderate Risk"
    else:
        return "Low Risk"

# Classify every sensor reading
df["temperature_risk"] = df["temperature"].apply(classify_risk)

# Summarize risk by shipment
risk_summary = df.groupby(
    ["shipment_id", "product", "origin", "destination"]
).agg(
    average_temperature=("temperature", "mean"),
    highest_temperature=("temperature", "max"),
    high_risk_readings=("temperature_risk",
                        lambda x: (x == "High Risk").sum()),
    moderate_risk_readings=("temperature_risk",
                            lambda x: (x == "Moderate Risk").sum()),
    low_risk_readings=("temperature_risk",
                       lambda x: (x == "Low Risk").sum())
).reset_index()

# Save results
output_file = "data/processed/spoilage_risk_report.csv"
risk_summary.to_csv(output_file, index=False)

print("\nShipment Risk Report:")
print(risk_summary.to_string(index=False))

print("\nRisk analysis completed successfully!")
print("Report saved to:", output_file)
