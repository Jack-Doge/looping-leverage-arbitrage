# Looping Leverage Arbitrage Simulation

This folder contains various DeFi looping leverage arbitrage and compound interest simulation scripts, suitable for academic research, strategy analysis, and educational demonstration.

## Contents

### 1. simple_compound_curve.py
- Simulates the compound interest growth curve for a single initial investment (no leverage, no looping), showing profit changes over different days.

### 2. fixed_layers_profit_bar.py
- For a single initial investment, simulates a fixed number of leverage loops (e.g., 10 layers), calculates cumulative profit for each layer, and presents the results as a bar chart.

### 3. dynamic_leverage_profit_vs_investment.py
- Simulates dynamic leverage looping for various initial investments, automatically determining the maximum feasible loop count, and plots the final profit and leverage multiplier as line charts.

### 4. dynamic_leverage_apy_liquidation.py
- Simulates dynamic leverage looping for various initial investments, plotting both the estimated annualized APY and liquidation threshold (or percentage) in two subplots. Useful for observing how capital size affects liquidation risk.

## Who is this for?
- Researchers, developers, and students interested in DeFi looping leverage arbitrage, capital efficiency, and liquidation risk.

## How to use
1. Install Python 3 and dependencies such as matplotlib and numpy.
2. Run any script in this folder:
   ```bash
   python script_name.py
   ```
3. The generated charts will be saved automatically in this folder.

---

To customize parameters (such as LTV, interest rates, fees, days, etc.), simply edit the parameter section at the top of each script.

---

> This project is for academic and strategy simulation purposes only. Do not use it for real financial operations. 