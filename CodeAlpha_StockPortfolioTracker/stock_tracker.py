stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker")

num_stocks = int(input("How many stocks do you want to enter? "))

for i in range(num_stocks):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock_name] * quantity

        total_investment += investment

        print("Investment in", stock_name, "=", investment)

    else:
        print("Stock not available")

print("\nTotal Investment Value =", total_investment)