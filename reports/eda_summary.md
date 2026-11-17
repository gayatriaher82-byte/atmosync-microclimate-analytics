
# AtmoSync - Exploratory Data Analysis Summary

## 1. Objective
To analyse simulated agricultural shipment sensor data and understand the temperature and humidity conditions of shipments.

## 2. Dataset Overview
- Total records: 15
- Total columns: 7
- Number of shipments: 3
- Data source: Python-based simulated sensor readings

## 3. Missing Value Analysis
No missing values were detected in the dataset.

## 4. Temperature Analysis
- Average temperature: 9.44°C
- Minimum temperature: 4.30°C
- Maximum temperature: 14.85°C

## 5. Humidity Analysis
- Average humidity: 73.03%
- Minimum humidity: 59.29%
- Maximum humidity: 87.93%

## 6. Shipment-wise Temperature Analysis
- SH001: 8.69°C
- SH002: 8.68°C
- SH003: 10.94°C

SH003 recorded the highest average temperature among the three shipments.

## 7. Key Observations
1. The dataset contains 15 simulated sensor readings.
2. All records have complete values.
3. SH003 has the highest average temperature.
4. Temperature and humidity vary across readings.

## 8. Limitations
- The dataset is simulated, not collected from physical sensors.
- Only three shipments are included.
- Temperature ranges are illustrative and are not validated spoilage thresholds.
- More data and product-specific storage guidelines are needed for reliable spoilage-risk analysis.

## 9. Conclusion
The initial EDA helped us understand the shipment dataset, check data completeness, and compare environmental conditions across shipments. These findings will support the next stages of AtmoSync, including data cleaning and spoilage-risk analysis.
