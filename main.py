import csv
import json 
from analyzer import calculate_return_statistics, calculate_returns, calculate_volatility

prices = {
    "Date": [],
    "AAPL": [],
    "MSFT": []
}

with open("data/prices.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        prices["Date"].append(row["Date"])
        prices["AAPL"].append(float(row["AAPL"]))
        prices["MSFT"].append(float(row["MSFT"]))

print(prices)

with open("data/report.json", "w") as file:
    aapl_returns = calculate_returns(prices["AAPL"])
    msft_returns = calculate_returns(prices["MSFT"])

    aapl_stats = calculate_return_statistics(aapl_returns)
    msft_stats = calculate_return_statistics(msft_returns)

    aapl_volatility = calculate_volatility(aapl_returns)
    msft_volatility = calculate_volatility(msft_returns)

    report = {
        "AAPL": {
            "average_return": aapl_stats[0],
            "best_return": aapl_stats[1],
            "worst_return": aapl_stats[2],
            "volatility": aapl_volatility
        },
        "MSFT": {
            "average_return": msft_stats[0],
            "best_return": msft_stats[1],
            "worst_return": msft_stats[2],
            "volatility": msft_volatility
        }
    }

    json.dump(report, file, indent=4)
