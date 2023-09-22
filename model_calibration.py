
import numpy as np
from scipy.optimize import minimize

def OU_likelihood(params, data):
    dt = 1
    mu, theta, sigma = params
    N = len(data)
    likelihood = -np.sum(np.log(sigma * np.sqrt(2 * np.pi * dt)) + 
                         (data[1:] - data[:-1] + theta * (mu - data[:-1]) * dt)**2 / (2 * sigma**2 * dt))
    return -likelihood

def calibrate_OU(data):
    # Initial guesses for mu, theta, and sigma
    initial_guess = [np.mean(data), 0.05, np.std(data)]
    # Minimize the negative log-likelihood
    results = minimize(OU_likelihood, initial_guess, args=(data), method='L-BFGS-B', bounds=[(None, None), (0, None), (0, None)])
    # Extract the calibrated parameters
    mu_calibrated, theta_calibrated, sigma_calibrated = results.x
    return mu_calibrated, theta_calibrated, sigma_calibrated

if __name__ == "__main__":
    from data_generation import generate_synthetic_data
    S1, S2_adjusted = generate_synthetic_data()
    spread_data = S2_adjusted - S1
    mu_calibrated, theta_calibrated, sigma_calibrated = calibrate_OU(spread_data)
    print(f"Calibrated Parameters - mu: {mu_calibrated}, theta: {theta_calibrated}, sigma: {sigma_calibrated}")
