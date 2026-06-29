def calculate_returns(price_list):
    returns = []
    for i in range(1, len(price_list)):
        ret = (price_list[i] - price_list[i-1]) / price_list[i-1]
        returns.append(ret)
    return returns

def calculate_return_statistics(returns):
    mean_return = sum(returns) / len(returns)
    max_return = max(returns)
    min_return = min(returns)
    return mean_return, max_return, min_return

def calculate_volatility(returns):
    mean_return = sum(returns) / len(returns)
    ret=0
    for i in returns:
        ret += (i-mean_return)**2
    variance = ret / len(returns)
    volatility = variance ** 0.5
    return volatility 
   



    