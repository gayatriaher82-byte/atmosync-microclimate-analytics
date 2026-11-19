
import pandas as pd

# Load shipment and market price data
shipments = pd.read_csv("data/processed/consumed_shipments.csv")
prices = pd.read_csv("data/processed/market_prices.csv")

print("AtmoSync: Agricultural Market Price Comparison")
print("------------------------------------------------")

# Get shipment details
shipment_info = shipments.groupby(
    ["shipment_id", "product", "destination"]
).size().reset_index().drop(columns=0)

# Find the highest price for each product
best_market = prices.loc[
    prices.groupby("product")["price_per_kg"].idxmax()
].rename(columns={
    "market": "best_market",
    "price_per_kg": "best_market_price"
})

# Find the price at each shipment's current destination
comparison = shipment_info.merge(
    prices,
    left_on=["product", "destination"],
    right_on=["product", "market"],
    how="left"
)

comparison = comparison.merge(
    best_market[["product", "best_market", "best_market_price"]],
    on="product",
    how="left"
)

comparison["potential_gain_per_kg"] = (
    comparison["best_market_price"] - comparison["price_per_kg"]
)

comparison["recommendation"] = comparison.apply(
    lambda row: "Consider rerouting"
    if row["potential_gain_per_kg"] > 0
    else "Keep current destination",
    axis=1
)

print("\nMarket Price Comparison:")
print(comparison.to_string(index=False))

# Save the report
output_file = "data/processed/market_price_comparison.csv"
comparison.to_csv(output_file, index=False)

print("\nMarket comparison completed successfully!")
print("Report saved to:", output_file)
