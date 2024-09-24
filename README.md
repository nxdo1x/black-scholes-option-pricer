# black-scholes-option-pricer
A Black-Scholes option pricer with PnL heatmap.

# Black-Scholes Option Pricer

## Description
This project implements the Black-Scholes option pricing model in Python. It provides users with the ability to calculate the theoretical price of European call and put options based on various input parameters, and visualize the profit and loss (PnL) using a heatmap.

## Features
- **Calculate Option Prices**: Inputs include stock price, strike price, volatility, time to expiration, and interest rate.
- **PnL Visualization**: Generates a heatmap displaying the PnL for call and put options, with colors indicating profitability (green for profit, red for loss).
- **User-Friendly Interface**: Built using Streamlit for an interactive experience.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/nxdo1x/black-scholes-option-pricer.git
   cd black-scholes-option-pricer

2. Install the required libraries:
   pip install streamlit matplotlib numpy pandas

3. Run the Streamlit app:
   streamlit run black_scholes_app.py

4. Open your web browser and go to http://localhost:8501 to access the app
   
5. Input the following parameters:

Stock Price: Current price of the stock.
Strike Price: The price at which the option can be exercised.
Volatility: The annualized standard deviation of the stock returns.
Time to Expiry: Time remaining until the option expires (in years).
Interest Rate: Risk-free interest rate.

6. Click the "Calculate" button to see the option prices and PnL heatmap.
  
7. Example Inputs
   Stock Price: 100
   Strike Price: 100
   Volatility: 20% (0.2)
   Time to Expiry: 0.5 years (6 months)
   Interest Rate: 5% (0.05)
