from sqlalchemy import create_engine

# Function to save inputs/outputs to MySQL database
def save_to_db(S, K, T, r, sigma, call_price, put_price, call_pnl, put_pnl):
    engine = create_engine('mysql+pymysql://username:password@localhost/db_name')
    with engine.connect() as connection:
        query = """
        INSERT INTO option_data (stock_price, strike_price, time_to_expiry, risk_free_rate, volatility, call_price, put_price, call_pnl, put_pnl)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        connection.execute(query, (S, K, T, r, sigma, call_price, put_price, call_pnl, put_pnl))

import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes pricing function
def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Streamlit input section
st.title('Black-Scholes Option Pricer with PnL Heatmap')

S = st.number_input('Stock Price', value=100.0)
K = st.number_input('Strike Price', value=100.0)
T = st.number_input('Time to Expiry (in years)', value=1.0)
r = st.number_input('Risk-Free Rate (as decimal)', value=0.05)
sigma = st.number_input('Volatility (as decimal)', value=0.2)
call_purchase_price = st.number_input('Call Purchase Price', value=10.0)
put_purchase_price = st.number_input('Put Purchase Price', value=5.0)

if st.button('Calculate'):
    # Calculate option prices
    call_price = black_scholes(S, K, T, r, sigma, "call")
    put_price = black_scholes(S, K, T, r, sigma, "put")
    
    # Calculate PnL
    call_pnl = call_price - call_purchase_price
    put_pnl = put_price - put_purchase_price
    
    st.write(f"Call Option Price: {call_price}")
    st.write(f"Put Option Price: {put_price}")
    st.write(f"Call PnL: {call_pnl}")
    st.write(f"Put PnL: {put_pnl}")

    # Save inputs and outputs to MySQL database
    save_to_db(S, K, T, r, sigma, call_price, put_price, call_pnl, put_pnl)

    # Create PnL heatmap
    pnl_data = np.array([[call_pnl, put_pnl]])
    fig, ax = plt.subplots()
    sns.heatmap(pnl_data, annot=True, cmap='RdYlGn', center=0, cbar=True, ax=ax)
    st.pyplot(fig)

