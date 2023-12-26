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
    Backtest the VaR model.
    
    :param historical_returns: A series of historical returns.
    :param var: The calculated VaR for the same period.
    :return: The percentage of days when the actual loss exceeded the VaR.
    """


def backtest_var(historical_returns, var):
    excedances = 0
    for return_value in historical_returns:
        if return_value < var:
            excedances += 1

    total_days = len(historical_returns)
    excendance_rate = excedances / total_days

    return excendance_rate


# ENHANCED BACKTESTING VAR
def enhanced_backtest_var(historical_data, confidence_level=0.95, rolling_window=252):
    excedances = 0
    var_values = []

    for i in range(rolling_window, len(historical_data)):
        window_data = historical_data.iloc[i-rolling_window:i]
        daily_returns = calculate_daily_returns(window_data)
        var = calculate_var(daily_returns, confidence_level)
        var_values.append(var)

        next_day_return = historical_data['Close'].pct_change().iloc[i]
        if next_day_return < var:
            excedances += 1

    excedances_rate = excedances / (len(historical_data) - rolling_window)
    return excedances_rate, var_values


"""
CALCULATIONG CONDITIONAL VaR
"""


def calculate_cvar(daily_returns, var, confidence_level=0.95):
    worse_than_var = daily_returns[daily_returns <= var]

    cvar = worse_than_var.mean()
    return cvar
