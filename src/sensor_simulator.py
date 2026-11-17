
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# AtmoSync - Agricultural Shipment Sensor Simulator

# Sample shipment information
shipments = [
    {"shipment_id": "SH001", "product": "Avocado", "origin": "Pune", "destination": "Mumbai"},
    {"shipment_id": "SH002", "product": "Mango", "origin": "Nashik", "destination": "Pune"},
    {"shipment_id": "SH003", "product": "Apple", "origin": "Shimla", "destination": "Delhi"}
]

# Generate simulated sensor readings
readings = []

start_time = datetime.now()

for shipment in shipments:
    for i in range(5):
        reading = {
            "shipment_id": shipment["shipment_id"],
            "product": shipment["product"],
            "origin": shipment["origin"],
            "destination": shipment["destination"],
            "temperature": round(np.random.uniform(4, 15), 2),
            "humidity": round(np.random.uniform(55, 90), 2),
            "timestamp": start_time + timedelta(minutes=10 * i)
        }

        readings.append(reading)

# Convert readings into a DataFrame
df = pd.DataFrame(readings)

# Display the simulated data
print("ATMoSync - SIMULATED SHIPMENT SENSOR DATA")
print(df)

# Save data as a CSV file
df.to_csv("data/raw/shipment_sensor_data.csv", index=False)

print("\nSensor data generated successfully!")
print("File saved in data/raw/shipment_sensor_data.csv")
