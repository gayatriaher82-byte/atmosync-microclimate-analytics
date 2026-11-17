
# AtmoSync – Agricultural Supply Chain Monitoring and Analytics

**Project Type:** Individual Data Analytics Internship Project  
**Project Domain:** Data Analytics and Data Engineering  
**Scope Version:** 2.0  
**Date:** 17 November 2026

## 1. Project Overview

AtmoSync is a real-time agricultural supply chain monitoring and analytics system designed to monitor the environmental conditions of agricultural shipments during transportation.

The system uses simulated IoT sensor data to monitor shipment conditions, identify containers experiencing abnormal environmental conditions, estimate spoilage risk, and compare alternative market opportunities.

It aims to help companies make data-driven decisions about agricultural shipments before product quality decreases.

## 2. Problem Statement

Agricultural products such as avocados can spoil during transportation when environmental conditions inside shipping containers become unsuitable.

An increase in temperature or other abnormal environmental conditions may increase the risk of product spoilage.

Companies need a system that can monitor shipment conditions, identify risky containers, estimate the remaining time before spoilage, and compare nearby market opportunities.

AtmoSync addresses this problem through data collection, processing, analytics, spoilage-risk estimation, and dashboard-based recommendations.

## 3. Aim

To develop an agricultural supply chain monitoring and analytics system that uses IoT sensor data and data analytics techniques to identify shipment risks, estimate spoilage time, compare market opportunities, and support better transportation decisions.

## 4. Objectives

- Develop a Python-based IoT sensor simulator.
- Generate environmental readings for agricultural shipment containers.
- Collect and process shipment sensor data.
- Design a data pipeline for handling incoming data.
- Store raw shipment data in a Snowflake data warehouse.
- Perform data cleaning and transformations using dbt.
- Calculate spoilage risk for agricultural shipments.
- Estimate the remaining time before product spoilage.
- Compare alternative markets and their prices.
- Develop a dashboard to display shipment conditions and analytical insights.
- Provide recommendations for potentially beneficial shipment rerouting.

## 5. Proposed System Components

### 5.1 Python IoT Sensor Simulator
Generates simulated sensor readings such as temperature and other environmental measurements for agricultural containers.

### 5.2 Apache Kafka Streaming Pipeline
Handles the flow of simulated sensor data through a data streaming pipeline.

### 5.3 Snowflake Data Warehouse
Stores incoming raw shipment data for further processing and analysis.

### 5.4 dbt Data Transformation
Cleans, organizes, and transforms raw data into analytical tables.

### 5.5 Spoilage Risk Calculation
Analyzes shipment conditions to identify containers at risk and estimate remaining spoilage time.

### 5.6 Analytical Dashboard
Displays important shipment metrics, market information, risk levels, and recommendations.

## 6. Key Performance Indicators (KPIs)

The project will focus on the following metrics specified in the training session:

1. **Active Containers:** Number of containers currently being monitored.
2. **Average Temperatures:** Average temperature readings across monitored containers.
3. **At-Risk Containers:** Number of containers identified as having elevated spoilage risk.
4. **Time to Spoilage:** Estimated remaining time before the goods may spoil.
5. **Market Price:** Price information for comparing alternative market opportunities.

The exact formulas and thresholds will be defined during implementation.

## 7. Proposed Methodology

1. Understand the agricultural spoilage problem.
2. Identify suitable shipment data and design the data schema.
3. Generate simulated IoT sensor readings using Python.
4. Stream sensor data through Apache Kafka.
5. Store raw data in Snowflake.
6. Clean and transform data using dbt.
7. Perform analytical processing using Python and SQL.
8. Calculate spoilage risk and estimated time to spoilage.
9. Compare alternative market prices and opportunities.
10. Develop an analytical dashboard.
11. Generate insights and recommendations.
12. Test and document the complete system.

## 8. Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Sensor simulation and analytics |
| Apache Kafka | Data streaming |
| Snowflake | Data warehouse |
| dbt | Data transformation |
| SQL | Data querying and analysis |
| Apache Superset | Dashboard visualization |

Power BI or Tableau may also be considered for dashboard development, as permitted in the training session.

## 9. Expected Outcomes

- A working Python-based shipment sensor simulator.
- A dataset containing agricultural shipment readings.
- A data streaming and processing pipeline.
- Organized and transformed analytical data.
- Spoilage-risk identification and estimation.
- Comparison of alternative market opportunities.
- An interactive analytical dashboard.
- Data-driven shipment monitoring and rerouting recommendations.
- Final project documentation and demonstration.

## 10. Four-Week Development Plan

**Week 1 – Data Collection and Infrastructure**
- Understand the agricultural spoilage problem.
- Design the data schema.
- Develop the Python sensor simulator.

**Week 2 – Data Pipelines**
- Implement the data pipeline.
- Create Snowflake raw tables.
- Perform data cleaning and dbt transformations.
- Develop a basic dashboard.
- Prepare for MID project review.

**Week 3 – Advanced Analytics**
- Calculate time to spoilage.
- Estimate shipment spoilage risk.
- Identify high-risk containers.
- Implement business logic.

**Week 4 – Automation and Finalization**
- Optimize Snowflake queries.
- Configure automated alerts.
- Complete the dashboard.
- Test and prepare the final project demonstration.

## 11. Scope and Assumptions

- The project will initially use simulated IoT sensor readings.
- Historical or synthetic datasets may be used instead of physical IoT sensors.
- A small dataset will be preferred during initial development.
- Agricultural shipments, such as avocado transportation, will be used as the example business scenario.
- Actual spoilage thresholds, estimation formulas, market data sources, and rerouting rules will be finalized during implementation.

## 12. Current Project Status

The initial GitHub repository and project structure have been created. The project scope has been updated according to the official Infotact training session.

The next development milestone is to design the shipment data schema and create the Python-based IoT sensor simulator.

---

**Project Name:** AtmoSync – Agricultural Supply Chain Monitoring and Analytics  
**Project Category:** Data Analytics  
**Project Mode:** Individual
