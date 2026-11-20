# AtmoSync — Intelligent Shipment Rerouting

## 1. Introduction

AtmoSync is an agricultural supply-chain monitoring and analytics project designed to help monitor shipments and reduce product spoilage.

The Intelligent Shipment Rerouting module helps identify better destination markets for shipments based on transportation costs, market prices, estimated travel time, and spoilage risk.

The module aims to recommend routes that are both financially beneficial and feasible within the remaining safe time of agricultural products.

## 2. Objectives

- Identify suitable alternative markets for shipments.
- Compare agricultural market prices.
- Consider transportation costs.
- Estimate travel time to alternative destinations.
- Evaluate spoilage risk before recommending rerouting.
- Generate rerouting recommendations for better shipment decisions.

## 3. Working Methodology

The Intelligent Shipment Rerouting module uses Python and Pandas to analyse shipment information and identify suitable alternative destinations.

The working process consists of the following steps:

### Step 1: Load Input Data

The module loads four CSV files:

- `consumed_shipments.csv` – Contains shipment information and sensor records.
- `market_prices.csv` – Contains agricultural product prices in different markets.
- `transport_costs.csv` – Contains transportation costs and estimated travel hours.
- `spoilage_time_estimates.csv` – Contains estimated remaining safe time and spoilage status.

### Step 2: Identify Latest Shipment Records

The module sorts shipment records using timestamps and selects the latest record for each shipment ID.

### Step 3: Evaluate Spoilage Time

The estimated remaining safe time is checked for every shipment.

If the remaining time is zero or negative, the shipment is marked for immediate inspection.

### Step 4: Identify Alternative Destinations

The module matches available market prices with transportation routes based on the shipment's product and origin.

The shipment's origin is excluded as an alternative destination.

### Step 5: Calculate Net Value

The net value per kilogram is calculated using:

**Net Value per kg = Market Price per kg − Transportation Cost per kg**

### Step 6: Validate Estimated Travel Time

The module compares the estimated travel time with the remaining safe time of the shipment.

Only routes that can be completed within the estimated remaining safe time are considered feasible.

### Step 7: Select the Best Destination

Among feasible routes, the module selects the destination with the highest net value per kilogram.

It then compares this option with the current destination to determine whether rerouting should be considered.

### Step 8: Generate Recommendations

The module generates recommendations such as:

- Consider rerouting.
- Keep current destination.
- Critical – Immediate inspection required.
- Critical – No alternative route can arrive in time.
- No alternative destination available.

## 4. Output Generated

After completing the rerouting analysis, the module generates a CSV report named:

`rerouting_recommendations.csv`

The report contains:

- Shipment ID
- Product name
- Current destination
- Recommended destination
- Market price per kilogram
- Transportation cost per kilogram
- Net value per kilogram
- Estimated travel hours
- Estimated remaining safe hours
- Spoilage status
- Final decision

The generated report is saved inside:

`data/processed/`

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data processing and analysis |
| CSV | Input and output data storage |

## 6. Conclusion

The Intelligent Shipment Rerouting module improves agricultural shipment decision-making by combining market price analysis, transportation costs, estimated travel time, and spoilage information.

It helps identify financially beneficial and time-feasible destinations while highlighting shipments that require immediate attention.

This module contributes to reducing potential agricultural product losses and improving supply-chain efficiency in the AtmoSync project.
