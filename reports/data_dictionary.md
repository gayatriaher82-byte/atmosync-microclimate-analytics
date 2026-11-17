# AtmoSync – Data Dictionary

## Project Description
This document defines the fields required to monitor agricultural shipments and analyze their spoilage risk.

## Shipment Data Fields

| Field Name | Data Type | Description | Example |
|---|---|---|---|
| shipment_id | String | Unique shipment identifier | SH001 |
| product | String | Name of agricultural product | Avocado |
| origin | String | Shipment starting location | Pune |
| destination | String | Planned delivery location | Mumbai |
| temperature | Float | Temperature inside the container in °C | 8.5 |
| humidity | Float | Humidity inside the container in % | 75.0 |
| timestamp | DateTime | Date and time of sensor reading | 2026-11-17 10:30:00 |
| market_price | Float | Market selling price per kg | 120.0 |
| quantity_kg | Float | Total shipment quantity in kilograms | 500.0 |

## Purpose of the Data

- Monitor environmental conditions during transportation.
- Identify unusual temperature and humidity readings.
- Analyze shipment conditions over time.
- Estimate spoilage risk using product-specific rules.
- Compare market opportunities for possible rerouting.

## Notes

- The example values are illustrative, not actual sensor readings.
- Temperature and humidity thresholds must be selected using reliable product-specific sources or mentor guidance.
- Market prices should be linked to a source and date when real data is used.
- Additional fields may be added as the project develops.
