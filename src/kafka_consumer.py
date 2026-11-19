
import json
import csv
import os
from kafka import KafkaConsumer

# Create output directory
os.makedirs("data/processed", exist_ok=True)

output_file = "data/processed/consumed_shipments.csv"

# Connect to Kafka
consumer = KafkaConsumer(
    "shipment-sensor-data",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="atmosync-consumer-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

print("AtmoSync: Kafka Consumer Started!")
print("Waiting for shipment records...")

try:
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "shipment_id",
            "product",
            "origin",
            "destination",
            "temperature",
            "humidity",
            "timestamp"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for message in consumer:
            shipment = message.value
            writer.writerow(shipment)
            file.flush()

            print("Received:", shipment)
            print("Saved to:", output_file)

except KeyboardInterrupt:
    print("\nConsumer stopped by user.")

finally:
    consumer.close()
    print("Kafka Consumer Closed.")
