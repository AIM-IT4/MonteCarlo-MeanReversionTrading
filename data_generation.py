
import numpy as np

def generate_synthetic_data():
    # Set random seed for reproducibility
    np.random.seed(42)

    # Simulation parameters
    T = 252  # number of trading days in a year
    dt = 1  # time increment (1 day)
    N = T * 1  # Total number of days for which we're generating data
    mu1, mu2 = 0.0002, 0.0003  # daily returns for asset 1 and 2
    sigma1, sigma2 = 0.02, 0.025  # daily volatility for asset 1 and 2
    S1_0, S2_0 = 100, 110  # initial prices for asset 1 and 2

    # Generate paths for asset 1 and 2 using geometric Brownian motion
    W1 = np.random.randn(N) * np.sqrt(dt)
    W2 = np.random.randn(N) * np.sqrt(dt)
    S1 = S1_0 * np.exp(np.cumsum((mu1 - 0.5 * sigma1**2) * dt + sigma1 * W1))
    S2 = S2_0 * np.exp(np.cumsum((mu2 - 0.5 * sigma2**2) * dt + sigma2 * W2))

    # Generate synthetic mean-reverting spread using Ornstein-Uhlenbeck process
    theta = 0.05  # speed of mean-reversion
    mean_spread = 5  # equilibrium level
    sigma_spread = 2  # volatility of spread
    spread = np.zeros(N)
    spread[0] = S2[0] - S1[0]
    for t in range(1, N):
        spread[t] = spread[t-1] + theta * (mean_spread - spread[t-1]) * dt + sigma_spread * np.sqrt(dt) * np.random.randn()

    # Add the spread to asset 2's price
    S2_adjusted = S1 + spread

    return S1, S2_adjusted

if __name__ == "__main__":
    S1, S2_adjusted = generate_synthetic_data()
    print("Data generated successfully!")
