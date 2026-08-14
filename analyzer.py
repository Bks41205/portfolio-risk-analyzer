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
   
def cumulative_return(prices_list):
    if not prices_list:
        return 0.0
    cumulative_ret = (prices_list[-1] - prices_list[0]) / prices_list[0]
    return cumulative_ret


def portfolio_return(weights,returns):
    portfolio_ret = sum(w * r for w, r in zip(weights, returns))
    return portfolio_ret


def calculate_covariance(returns_a, returns_b):
    mean_a = sum(returns_a) / len(returns_a)
    mean_b = sum(returns_b) / len(returns_b)
    cov = sum((a - mean_a) * (b - mean_b) for a, b in zip(returns_a, returns_b))
    return cov / len(returns_a)

def portfolio_volatility(weights, volatilities, covariance):
    w1, w2 = weights
    v1, v2 = volatilities
    variance = (w1**2 * v1**2) + (w2**2 * v2**2) + (2 * w1 * w2 * covariance)
    return variance ** 0.5



    