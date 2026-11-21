
# AtmoSync - Shipment Data Schema

## 1. Purpose
This document defines the structure of shipment sensor data
used in the AtmoSync agricultural supply-chain monitoring system.

## 2. Dataset Fields

| Field Name | Data Type | Description | Unit |
|---|---|---|---|
| shipment_id | String | Unique shipment identifier | - |
| product | String | Agricultural product name | - |
| origin | String | Shipment starting location | - |
| destination | String | Shipment destination | - |
| temperature | Float | Temperature inside shipment | Celsius (°C) |
| humidity | Float | Humidity inside shipment | Percentage (%) |
| timestamp | Datetime | Date and time of sensor reading | - |

## 3. Dataset Information
- Source: Python IoT sensor simulator
- Storage format: CSV
- Current records: 15
- Current columns: 7

## 4. Data Quality
- Missing values: 0
- Duplicate records: 0
- Invalid humidity records: 0
- Invalid timestamps: 0
- Missing or non-numeric temperatures: 0

## 5. Future Usage
This schema will be used for:
- Kafka data streaming
- Snowflake data storage
- dbt transformations
- Shipment condition monitoring
- Spoilage-risk analysis
