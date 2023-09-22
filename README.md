
# Monte Carlo Simulation for Trading Under a Lévy-Driven Mean-Reverting Framework

## Overview
This project explores the application of Monte Carlo simulations in a Lévy-driven mean-reverting framework for pairs trading. We use synthetic data to demonstrate the methodology and backtest a trading strategy.

## Data
The synthetic data is generated to represent two assets with a mean-reverting spread. The spread is modeled using the Ornstein-Uhlenbeck process.

## Methodology

### Data Generation
- Synthetic data is generated using the `data_generation.py` script.
- The spread between the two assets is modeled using an Ornstein-Uhlenbeck process.

### Model Calibration
- The Ornstein-Uhlenbeck process is calibrated to the synthetic spread data using the `model_calibration.py` script.

### Monte Carlo Simulation
- Potential future paths for the spread are simulated using the calibrated Ornstein-Uhlenbeck process.
- Simulations are performed using the `monte_carlo_simulation.py` script.

### Backtesting
- A pairs trading strategy is backtested on the synthetic data using thresholds determined from the Monte Carlo simulations.
- Backtesting is performed using the `backtesting.py` script.

## Results
The project demonstrates how to use Monte Carlo simulations in a mean-reverting framework for pairs trading. The strategy shows positive returns on the synthetic data, but it's essential to consider real-world factors and risks when applying to actual trading scenarios.

## How to Run
1. Generate synthetic data using `data_generation.py`.
2. Calibrate the model using `model_calibration.py`.
3. Run Monte Carlo simulations using `monte_carlo_simulation.py`.
4. Backtest the strategy using `backtesting.py`.


## Contact
For questions, feedback, or contributions, please open an issue or submit a pull request.
