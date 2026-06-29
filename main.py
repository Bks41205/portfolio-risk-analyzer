import csv

with open("data/prices.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)