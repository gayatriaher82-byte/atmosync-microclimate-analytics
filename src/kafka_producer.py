
import json
import time
import pandas as pd
from kafka import KafkaProducer

# Connect Python to Kafka
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

# Read existing cleaned shipment data
df = pd.read_csv("data/processed/cleaned_shipment_data.csv")

print("AtmoSync: Sending shipment sensor data to Kafka...")

try:
    for _, row in df.iterrows():
        shipment = {
            "shipment_id": str(row["shipment_id"]),
            "product": str(row["product"]),
            "origin": str(row["origin"]),
            "destination": str(row["destination"]),
            "temperature": float(row["temperature"]),
            "humidity": float(row["humidity"]),
            "timestamp": str(row["timestamp"])
        }

        producer.send("shipment-sensor-data", value=shipment)
        print("Sent:", shipment)

        time.sleep(1)

    producer.flush()
    print("\nAll shipment records sent successfully!")

except Exception as error:
    print("Error:", error)

finally:
    producer.close()
