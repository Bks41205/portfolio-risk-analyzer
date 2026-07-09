import csv
import json
from analyzer import (
    calculate_return_statistics,
    calculate_returns,
    calculate_volatility,
)

prices = {}


with open("data/prices.csv", "r") as file:
    reader = csv.DictReader(file)

   
    for header in reader.fieldnames:
        prices[header] = []

   
    for row in reader:
        for header, value in row.items():
            if header == "Date":
                prices[header].append(value)
            else:
                prices[header].append(float(value))

print("Reading stock prices...")
print("Calculating returns and risk metrics...")

report = {}


for ticker in prices.keys():

    
    if ticker == "Date":
        continue

    stock_prices = prices[ticker]

    returns = calculate_returns(stock_prices)

    mean_return, max_return, min_return = calculate_return_statistics(returns)

    volatility = calculate_volatility(returns)

    report[ticker] = {
        "average_return": mean_return,
        "best_return": max_return,
        "worst_return": min_return,
        "volatility": volatility,
    }


with open("reports/report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Report saved to reports/report.json")