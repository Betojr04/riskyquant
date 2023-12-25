import numpy as np

"""
Everything below this is calculating VaR
"""

# 1st step is to calculate daily returns


def calculate_daily_returns(data):
    try:
        if 'Close' in data.columns:
            daily_returns = data['Close'].pct_change()
            return daily_returns.dropna()
        else:
            print("Data does not contain 'Close' column.")
            return None
    except Exception as e:
        print(f"Error in calculating daily returns {e}")
        return None

# calculating 1-day VaR @ 95% confidence level using historical data


def calculate_var(daily_returns, confidence_level=0.95):
    # Sort returns in ascending order
    sorted_returns = np.sort(daily_returns)

    # Find the percentile
    index = int((1 - confidence_level) * len(sorted_returns))
    var = sorted_returns[index]
    return var


"""
CALCULATIONG CONDITIONAL VaR
"""


def calculate_cvar(daily_returns, var, confidence_level=0.95):
    worse_than_var = daily_returns[daily_returns <= var]

    cvar = worse_than_var.mean()
    return cvar
