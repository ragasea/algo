# Prompt: Python Trading Strategy v1 for Master Quant Hub
# Date: Thursday, April 2, 2026 | Time: 10:15 AM IST

import pandas as pd
import pandas_ta as ta
import yfinance as yf

def execute_strategy(symbol):
    print(f"🚀 Analyzing {symbol} for Master...")
    # Fetching latest 1-day data for indicators
    df = yf.download(symbol, period="5d", interval="1h")
    
    # Technical Indicators: RSI and EMA
    df['RSI'] = ta.rsi(df['Close'], length=14)
    df['EMA_20'] = ta.ema(df['Close'], length=20)
    
    last_rsi = df['RSI'].iloc[-1]
    last_close = df['Close'].iloc[-1]
    last_ema = df['EMA_20'].iloc[-1]
    
    print(f"Current Price: {last_close} | RSI: {last_rsi:.2f}")
    
    # Logic: Buy if RSI < 30 (Oversold) and Price > EMA_20
    if last_rsi < 40 and last_close > last_ema:
        print(f"✅ BUY SIGNAL DETECTED FOR {symbol}")
        # Add API execution logic here
    else:
        print(f"❌ No clear signal for {symbol} yet.")

if __name__ == "__main__":
    assets = ["RELIANCE.NS", "HDFCBANK.NS", "BTC-USD"]
    for asset in assets:
        execute_strategy(asset)
