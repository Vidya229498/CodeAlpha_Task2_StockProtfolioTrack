stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 120,
    "MSFT": 300,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print(" Welcome to Stock Portfolio Tracker!")
print("Available stocks and their prices (USD):")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
print("\nEnter your stocks. Type 'done' to finish.\n")

# Taking user input for stocks
while True:
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print(" Stock not found! Please choose from the list.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print(" Please enter a positive number.\n")
            continue
    except ValueError:
        print(" Invalid input! Please enter a number.\n")
        continue

    # Calculate and store value
    value = stock_prices[stock_name] * quantity
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    total_investment += value

    print(f"✅ Added {quantity} of {stock_name} worth ${value}\n")

# Display results
print("\n===== Portfolio Summary =====")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    print(f"{stock} - {qty} shares × ${price} = ${value}")
print("==============================")
print(f" Total Investment: ${total_investment}")
print("==============================")

# Optional: Save to text file
save = input("\nDo you want to save the result to a file? (y/n): ").lower()
if save == "y":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("========================\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock} - {qty} shares × ${price} = ${value}\n")
        file.write("========================\n")
        file.write(f"Total Investment: ${total_investment}\n")
    print(" Results saved to 'portfolio_summary.txt'.")

print("\n Thank you for using the Stock Portfolio Tracker!")