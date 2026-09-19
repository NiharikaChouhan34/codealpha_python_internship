stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks:", ", ".join(stock_prices.keys()))

total_investment = 0

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the listed stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Stock price:", stock_prices[stock])
        print("Investment for", stock, ":", investment)

    except ValueError:
        print("Please enter a valid whole number.")

print("\nTotal Investment Value:", total_investment)

with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("Total Investment Value: " + str(total_investment))

print("Result saved in portfolio_result.txt")
