
import numpy as np

def backtest_strategy(data, upper_threshold, lower_threshold, transaction_cost=5):
    initial_capital = 100000  # Starting capital
    position = 0  # 1 for long spread, -1 for short spread, 0 for no position
    capital = initial_capital
    capital_history = [capital]

    # Loop through the data for backtesting
    for t in range(1, len(data)):
        current_spread = data[t]
        previous_spread = data[t-1]

        # Check conditions to enter or exit trades
        if position == 0:  # No current position
            if current_spread < lower_threshold[t]:  # Enter long spread position
                position = 1
                capital -= transaction_cost
            elif current_spread > upper_threshold[t]:  # Enter short spread position
                position = -1
                capital -= transaction_cost

        elif position == 1:  # Currently long the spread
            if current_spread > np.mean(data):  # Exit position when spread reverts to the mean
                position = 0
                capital += transaction_cost
            capital += position * (current_spread - previous_spread) * 100  # Assume trading 100 units

        elif position == -1:  # Currently short the spread
            if current_spread < np.mean(data):  # Exit position when spread reverts to the mean
                position = 0
                capital += transaction_cost
            capital += position * (current_spread - previous_spread) * 100

        capital_history.append(capital)
    
    return capital_history

if __name__ == "__main__":
    from data_generation import generate_synthetic_data
    from monte_carlo_simulation import simulate_OU_paths
    from model_calibration import calibrate_OU
    S1, S2_adjusted = generate_synthetic_data()
    spread_data = S2_adjusted - S1
    mu_calibrated, theta_calibrated, sigma_calibrated = calibrate_OU(spread_data)
    simulated_paths = simulate_OU_paths(mu_calibrated, theta_calibrated, sigma_calibrated, spread_data[-1])
    mean_simulated_spread = np.mean(simulated_paths, axis=1)
    std_simulated_spread = np.std(simulated_paths, axis=1)
    upper_threshold = mean_simulated_spread + std_simulated_spread
    lower_threshold = mean_simulated_spread - std_simulated_spread
    capital_history = backtest_strategy(spread_data, upper_threshold, lower_threshold)
    print(f"Final Portfolio Value: {capital_history[-1]}")
