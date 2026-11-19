
import pandas as pd

shipments = pd.read_csv("data/processed/consumed_shipments.csv")
market_prices = pd.read_csv("data/processed/market_prices.csv")
transport_costs = pd.read_csv("data/processed/transport_costs.csv")
spoilage = pd.read_csv("data/processed/spoilage_time_estimates.csv")

print("AtmoSync: Intelligent Shipment Rerouting")
print("----------------------------------------")

latest = shipments.sort_values("timestamp").groupby(
    "shipment_id"
).tail(1)

latest = latest.merge(
    spoilage[
        ["shipment_id", "estimated_hours_remaining", "status"]
    ],
    on="shipment_id",
    how="left"
)

recommendations = []

for _, shipment in latest.iterrows():

    remaining_time = shipment["estimated_hours_remaining"]

    # Critical shipments need immediate inspection
    if remaining_time <= 0:
        recommendations.append({
            "shipment_id": shipment["shipment_id"],
            "product": shipment["product"],
            "current_destination": shipment["destination"],
            "recommended_destination": "Immediate inspection",
            "estimated_travel_hours": None,
            "estimated_hours_remaining": remaining_time,
            "net_value_per_kg": None,
            "spoilage_status": shipment["status"],
            "decision": "Critical - Immediate inspection required"
        })
        continue

    # Get possible markets and routes
    possible_markets = market_prices[
        market_prices["product"] == shipment["product"]
    ]

    possible_routes = transport_costs[
        transport_costs["origin"] == shipment["origin"]
    ]

    options = possible_markets.merge(
        possible_routes,
        left_on="market",
        right_on="destination"
    )

    # Exclude the shipment's origin as a destination
    options = options[
        options["destination"] != shipment["origin"]
    ].copy()

    if options.empty:
        decision = "No alternative destination available"
        best = None
    else:
        options["net_value_per_kg"] = (
            options["price_per_kg"]
            - options["transport_cost_per_kg"]
        )

        # Only routes that fit within the estimated remaining time
        feasible = options[
            options["estimated_travel_hours"] <= remaining_time
        ]

        if feasible.empty:
            decision = "Critical - No alternative route can arrive in time"
            best = options.loc[
                options["estimated_travel_hours"].idxmin()
            ]
        else:
            best = feasible.loc[
                feasible["net_value_per_kg"].idxmax()
            ]

            current = feasible[
                feasible["destination"] == shipment["destination"]
            ]

            if current.empty:
                decision = "Consider rerouting - Current route is not feasible"
            elif (
                best["net_value_per_kg"]
                > current.iloc[0]["net_value_per_kg"]
            ):
                decision = "Consider rerouting"
            else:
                decision = "Keep current destination"

    if best is None:
        recommendations.append({
            "shipment_id": shipment["shipment_id"],
            "product": shipment["product"],
            "current_destination": shipment["destination"],
            "recommended_destination": "None",
            "estimated_travel_hours": None,
            "estimated_hours_remaining": remaining_time,
            "net_value_per_kg": None,
            "spoilage_status": shipment["status"],
            "decision": decision
        })
    else:
        recommendations.append({
            "shipment_id": shipment["shipment_id"],
            "product": shipment["product"],
            "current_destination": shipment["destination"],
            "recommended_destination": best["destination"],
            "market_price_per_kg": best["price_per_kg"],
            "transport_cost_per_kg": best["transport_cost_per_kg"],
            "net_value_per_kg": best["net_value_per_kg"],
            "estimated_travel_hours": best["estimated_travel_hours"],
            "estimated_hours_remaining": remaining_time,
            "spoilage_status": shipment["status"],
            "decision": decision
        })

result = pd.DataFrame(recommendations)

print("\nImproved Rerouting Recommendations:")
print(result.to_string(index=False))

output_file = "data/processed/rerouting_recommendations.csv"
result.to_csv(output_file, index=False)

print("\nRerouting analysis completed successfully!")
print("Report saved to:", output_file)
