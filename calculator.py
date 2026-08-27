def calculate_etsy_profit(item_price, shipping_charge, item_cost, shipping_cost, offsite_ads=False):
    revenue = item_price + shipping_charge
    
    # Etsy Standard Fees
    listing_fee = 0.20
    transaction_fee = revenue * 0.065
    payment_processing = (revenue * 0.03) + 0.25
    
    # Optional Offsite Ads Fee (15%)
    ads_fee = revenue * 0.15 if offsite_ads else 0.0
    
    total_fees = listing_fee + transaction_fee + payment_processing + ads_fee
    total_costs = item_cost + shipping_cost + total_fees
    net_profit = revenue - total_costs
    profit_margin = (net_profit / revenue) * 100 if revenue > 0 else 0
    
    return {
        "Revenue": round(revenue, 2),
        "Total Etsy Fees": round(total_fees, 2),
        "Net Profit": round(net_profit, 2),
        "Profit Margin (%)": round(profit_margin, 2)
    }

if __name__ == "__main__":
    print("--- Etsy Profit & Fee Calculator ---")
    price = float(input("Item Selling Price ($): "))
    ship_charge = float(input("Shipping Charged to Buyer ($): "))
    cost = float(input("Item Material/Production Cost ($): "))
    ship_cost = float(input("Actual Shipping Cost ($): "))
    
    result = calculate_etsy_profit(price, ship_charge, cost, ship_cost)
    
    print("\n--- Summary ---")
    for key, val in result.items():
        print(f"{key}: {val}")
