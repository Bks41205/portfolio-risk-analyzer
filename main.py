import csv

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