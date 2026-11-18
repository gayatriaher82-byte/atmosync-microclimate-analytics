# AtmoSync - Kafka Streaming Integration

## 1. Overview
Apache Kafka is used to stream shipment sensor data for real-time processing in AtmoSync.

## 2. Kafka Setup
- Kafka Version: 4.4.0
- Environment: WSL2 Ubuntu
- Broker: localhost:9092
- Topic: shipment-sensor-data

## 3. Python Integration
- Python library: kafka-python 3.0.13
- Producer file: src/kafka_producer.py
- Input dataset: data/processed/cleaned_shipment_data.csv

## 4. Data Streaming
The Python producer reads cleaned shipment sensor records and sends them to the Kafka topic.

Each record contains:
- Shipment ID
- Product
- Origin
- Destination
- Temperature
- Humidity
- Timestamp

A one-second delay is used between records during testing.

## 5. Testing and Verification
- Successfully sent 15 records from the cleaned CSV using Python.
- Verified the records using the Kafka console consumer.
- Also sent one manual test message.
- Confirmed that the consumer received 16 messages in total.

## 6. Current Progress
Python-to-Kafka integration has been successfully tested.

The current implementation streams existing CSV records sequentially. Continuous live sensor ingestion and downstream analytics are future development tasks.
