# AtmoSync Snowflake Data Warehouse Setup

## Date
23 November 2026

## Platform
Snowflake Cloud Data Warehouse

## Setup Completed

1. Created database: ATMOSYNC_DB
2. Created schema: RAW_DATA
3. Created table: SHIPMENT_SENSOR_DATA
4. Created CSV file format: SHIPMENT_CSV_FORMAT
5. Created internal stage: SHIPMENT_STAGE

## Table Structure

- SHIPMENT_ID
- PRODUCT
- ORIGIN
- DESTINATION
- TEMPERATURE
- HUMIDITY
- TIMESTAMP

## Verification

Successfully executed the Snowflake setup SQL script.
Verified that SHIPMENT_SENSOR_DATA exists in the RAW_DATA schema.

## Pending Tasks

1. Upload shipment_sensor_data.csv.
2. Load CSV records into SHIPMENT_SENSOR_DATA.
3. Verify the loaded records.
4. Continue Snowflake data warehouse development.
