# AtmoSync Snowflake Data Warehouse Setup

## Date

23 November 2026

## Platform

Snowflake Cloud Data Warehouse

## Setup Completed

1. Created database: ATMOSYNC\_DB
2. Created schema: RAW\_DATA
3. Created table: SHIPMENT\_SENSOR\_DATA
4. Created CSV file format: SHIPMENT\_CSV\_FORMAT
5. Created internal stage: SHIPMENT\_STAGE

## Table Structure

* SHIPMENT\_ID
* PRODUCT
* ORIGIN
* DESTINATION
* TEMPERATURE
* HUMIDITY
* TIMESTAMP

## Verification

Successfully executed the Snowflake setup SQL script.
Verified that SHIPMENT\_SENSOR\_DATA exists in the RAW\_DATA schema.

## Pending Tasks

1. Upload shipment\_sensor\_data.csv.
2. Load CSV records into SHIPMENT\_SENSOR\_DATA.
3. Verify the loaded records.
4. Continue Snowflake data warehouse development.

\## 24 November 2026 – Snowflake Progress



\- Reviewed the existing Snowflake setup documentation.

\- Continued documenting the Snowflake data warehouse development.

\- Reviewed the project's progress and planned the next development steps.

\- Updated the project documentation for progress tracking.



\*\*Status:\*\* Documentation updated successfully.

\## 25 November 2026 – Snowflake Data Loading and Verification



\- Located the shipment sensor dataset in `data/raw/shipment\_sensor\_data.csv`.

\- Uploaded the CSV file to Snowflake.

\- Loaded data into the existing `ATMOSYNC\_DB.RAW\_DATA.SHIPMENT\_SENSOR\_DATA` table.

\- Successfully inserted 15 rows.

\- Executed SQL COUNT query to verify the records.

\- Confirmed that the total record count is 15.

\- Viewed and verified the loaded shipment records.



\*\*Status:\*\* CSV data successfully loaded and verified in Snowflake.



\*\*Next Tasks:\*\*

\- Continue Snowflake data warehouse development.

\- Develop SQL-based shipment analytics.

\- Plan integration with dbt transformations.

