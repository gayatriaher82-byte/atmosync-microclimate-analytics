
import pandas as pd

# Load project datasets
shipments = pd.read_csv("data/processed/consumed_shipments.csv")
market_prices = pd.read_csv("data/processed/market_prices.csv")
transport_costs = pd.read_csv("data/processed/transport_costs.csv")
spoilage = pd.read_csv("data/processed/spoilage_time_estimates.csv")

print("AtmoSync: Intelligent Shipment Rerouting")
print("----------------------------------------")

# Get the latest reading for every shipment
latest = shipments.sort_values("timestamp").groupby(
    "shipment_id"
).tail(1)

# Attach spoilage estimates
latest = latest.merge(
    spoilage[
        ["shipment_id", "estimated_hours_remaining", "status"]
    ],
    on="shipment_id",
    how="left"
)

recommendations = []

for _, shipment in latest.iterrows():

    # Get available markets for this product
    possible_markets = market_prices[
        market_prices["product"] == shipment["product"]
    ]

    # Get available transport routes from shipment origin
    possible_routes = transport_costs[
        transport_costs["origin"] == shipment["origin"]
    ]

    # Match market column with destination column
    options = possible_markets.merge(
        possible_routes,
        left_on="market",
        right_on="destination"
    )

    if options.empty:
        continue

    # Calculate net value after transportation cost
    options["net_value_per_kg"] = (
        options["price_per_kg"]
        - options["transport_cost_per_kg"]
    )

    # Find the best market
    best = options.loc[
        options["net_value_per_kg"].idxmax()
    ]

    # Find the current destination's net value
    current = options[
        options["destination"] == shipment["destination"]
    ]

    current_value = (
        current.iloc[0]["net_value_per_kg"]
        if not current.empty else None
    )

    # Make recommendation
    if shipment["estimated_hours_remaining"] <= 0:
        decision = "Critical - Immediate inspection required"

    elif current_value is not None and (
        best["net_value_per_kg"] > current_value
    ):
        decision = "Consider rerouting"

    else:
        decision = "Keep current destination"

    recommendations.append({
        "shipment_id": shipment["shipment_id"],
        "product": shipment["product"],
        "current_destination": shipment["destination"],
        "recommended_destination": best["destination"],
        "best_market_price": best["price_per_kg"],
        "transport_cost": best["transport_cost_per_kg"],
        "net_value_per_kg": best["net_value_per_kg"],
        "estimated_hours_remaining":
            shipment["estimated_hours_remaining"],
        "spoilage_status": shipment["status"],
        "decision": decision
    })

# Create final report
result = pd.DataFrame(recommendations)

print("\nIntelligent Rerouting Recommendations:")
print(result.to_string(index=False))

# Save output
output_file = "data/processed/rerouting_recommendations.csv"
result.to_csv(output_file, index=False)

print("\nRerouting analysis completed successfully!")
print("Report saved to:", output_file)
