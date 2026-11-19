
import pandas as pd

input_file = "data/processed/consumed_shipments.csv"
df = pd.read_csv(input_file)

print("AtmoSync: Remaining Time-to-Spoilage Estimation")
print("------------------------------------------------")

# Demo critical temperature assumptions (in Celsius)
CRITICAL_TEMPERATURE = 12

# Assumed temperature rise per hour for this demonstration
TEMPERATURE_RISE_PER_HOUR = 2

summary = df.groupby(
    ["shipment_id", "product", "origin", "destination"]
).agg(
    current_temperature=("temperature", "last"),
    average_temperature=("temperature", "mean"),
    highest_temperature=("temperature", "max")
).reset_index()

def estimate_remaining_time(temperature):
    if temperature >= CRITICAL_TEMPERATURE:
        return 0
    return round(
        (CRITICAL_TEMPERATURE - temperature)
        / TEMPERATURE_RISE_PER_HOUR, 2
    )

summary["estimated_hours_remaining"] = (
    summary["current_temperature"].apply(estimate_remaining_time)
)

summary["status"] = summary["estimated_hours_remaining"].apply(
    lambda hours: "Critical" if hours == 0
    else "Warning" if hours <= 2
    else "Safe"
)

output_file = "data/processed/spoilage_time_estimates.csv"
summary.to_csv(output_file, index=False)

print("\nRemaining Time Estimates:")
print(summary.to_string(index=False))

print("\nEstimation completed successfully!")
print("Report saved to:", output_file)
