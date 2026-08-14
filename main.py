import csv
import json
from analyzer import (
    calculate_return_statistics,
    calculate_returns,
    calculate_volatility,
    cumulative_return,
    portfolio_return,
    calculate_covariance,
    portfolio_volatility,
    calculate_sharpe_ratio
) 
from visualizer import plot_correlation_heatmap, plot_cumulative_returns, plot_sharpe_ratios

if __name__ == "__main__":

 prices = {}

try:
    with open("data/prices.csv", "r") as file:
     reader = csv.DictReader(file)

   
     for header in reader.fieldnames:
            prices[header] = []

   
     for row in reader:
             for header, value in row.items():
                if header == "Date":
                  prices[header].append(value)
                else:
                  if value == "":
                   print("Error: Missing price value found.")
                   print(f"Column: {header}")
                   print("Please check data/prices.csv.")
                   exit(1)
                  try:
                     prices[header].append(float(value))
                    
                  except ValueError:
                      print("Error: Invalid value encountered in the CSV file. Please ensure all price values are numeric.\n")
                      exit(1)

except FileNotFoundError:
    print("Error: The file 'data/prices.csv' was not found.")
    exit(1)

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

    cumulative_ret = cumulative_return(stock_prices)

  


    

    report[ticker] = {
        "average_return": mean_return,
        "best_return": max_return,
        "worst_return": min_return,
        "volatility": volatility,
        "cumulative_return": cumulative_ret,
        
       
    }

    for other_ticker in prices.keys():
        if other_ticker == "Date" or other_ticker == ticker:
            continue

        other_stock_prices = prices[other_ticker]
        
        
        other_returns = calculate_returns(other_stock_prices)
        other_mean_return, _, _ = calculate_return_statistics(other_returns)
        other_volatility = calculate_volatility(other_returns)

        
        weights = [0.5, 0.5]
        port_return = portfolio_return(
            weights, 
            [mean_return, other_mean_return]
        )

        
        cov = calculate_covariance(returns, other_returns)
        port_volatility = portfolio_volatility(
            weights, 
            [volatility, other_volatility], 
            cov
        )

        port_sharpe_ratio = calculate_sharpe_ratio(port_return, port_volatility)

        
        report[ticker][f"portfolio_with_{other_ticker}"] = {
            "expected_return": port_return,
            "volatility": port_volatility
        }
        
        


with open("reports/report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Report saved to reports/report.json") 

print("Generating charts...")
plot_cumulative_returns(prices)
plot_correlation_heatmap(prices) 

print("Generating Sharpe Ratio chart...")
plot_sharpe_ratios(report)