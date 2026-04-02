# Prompt: Backtesting Engine for Master Quant Hub
# Date: Thursday, April 2, 2026 | Time: 10:40 AM IST
# Purpose: Test RSI < 40 & Price > EMA 20 Strategy on Historical Data

import pandas as pd
import yfinance as yf
import pandas_ta as ta

def run_backtest(symbol, period="1mo", interval="1h"):
    print(f"📊 Starting Backtest for: {symbol}")
    
    # 1. Fetch Data
    data = yf.download(symbol, period=period, interval=interval)
    if data.empty:
        print("❌ No data found.")
        return

    # 2. Setup Indicators
    data['RSI'] = ta.rsi(data['Close'], length=14)
    data['EMA_20'] = ta.ema(data['Close'], length=20)
    
    # 3. Simulation Variables
    initial_capital = 100000  # ₹1,00,000
    capital = initial_capital
    position = 0
    trade_log = []

    # 4. Loop through data (Backtest Logic)
    for i in range(1, len(data)):
        price = data['Close'].iloc[i]
        rsi = data['RSI'].iloc[i]
        ema = data['EMA_20'].iloc[i]
        
        # BUY Logic: RSI < 40 and Price > EMA_20
        if position == 0 and rsi < 40 and price > ema:
            position = capital / price
            capital = 0
            buy_price = price
            trade_log.append(f"BUY at {price:.2f}")

        # SELL Logic: RSI > 70 or Price < EMA_20 (Exit)
        elif position > 0 and (rsi > 70 or price < ema):
            capital = position * price
            position = 0
            profit = capital - initial_capital
            trade_log.append(f"SELL at {price:.2f} | Current Capital: ₹{capital:.2f}")

    # 5. Final Results
    final_value = capital if position == 0 else position * data['Close'].iloc[-1]
    total_return = ((final_value - initial_capital) / initial_capital) * 100
    
    print(f"--- Results for {symbol} ---")
    print(f"Starting Capital: ₹{initial_capital}")
    print(f"Final Value: ₹{final_value:.2f}")
    print(f"Total Return: {total_return:.2f}%")
    print(f"Total Trades: {len(trade_log)}")
    print("---------------------------\n")

if __name__ == "__main__":
    # Testing on Master's preferred Indian and Global assets
    test_assets = ["RELIANCE.NS", "HDFCBANK.NS", "BTC-USD", "GC=F"] # Gold
    for asset in test_assets:
        run_backtest(asset)
