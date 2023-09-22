
import numpy as np

def simulate_OU_paths(mu, theta, sigma, start_value, forecast_horizon=252, num_simulations=1000):
    dt = 1
    simulated_paths = np.zeros((forecast_horizon, num_simulations))
    for i in range(num_simulations):
        spread_path = [start_value]  # Start from the given start value
        for t in range(1, forecast_horizon):
            dW = np.random.randn() * np.sqrt(dt)
            dS = theta * (mu - spread_path[t-1]) * dt + sigma * dW
            spread_path.append(spread_path[t-1] + dS)
        simulated_paths[:, i] = spread_path
    return simulated_paths

if __name__ == "__main__":
    from data_generation import generate_synthetic_data
    from model_calibration import calibrate_OU
    S1, S2_adjusted = generate_synthetic_data()
    spread_data = S2_adjusted - S1
    mu_calibrated, theta_calibrated, sigma_calibrated = calibrate_OU(spread_data)
    simulated_paths = simulate_OU_paths(mu_calibrated, theta_calibrated, sigma_calibrated, spread_data[-1])
    print(f"Simulation completed for {simulated_paths.shape[1]} paths over {simulated_paths.shape[0]} days.")
