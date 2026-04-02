# Prompt: Master Quant Hub - Strategy & Dashboard Generator
# Date: Thursday, April 2, 2026 | Time: 12:15 PM IST

import yfinance as yf
import datetime

def get_market_data():
    # Fetching latest prices for Master
    assets = {
        "Nifty 50": "^NSEI",
        "HDFC Bank": "HDFCBANK.NS",
        "Reliance": "RELIANCE.NS",
        "Gold (10g)": "GC=F",
        "Bitcoin": "BTC-USD"
    }
    
    results = {}
    for name, ticker in assets.items():
        data = yf.Ticker(ticker).history(period="1d")
        if not data.empty:
            price = data['Close'].iloc[-1]
            # Convert Gold and BTC to INR for Master's preference
            if name == "Gold (10g)": price = (price / 31.1) * 10 * 93.03 # Approx conversion
            if name == "Bitcoin": price = price * 93.03
            results[name] = round(price, 2)
    return results

def update_dashboard(prices):
    now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Master Quant Hub 🔱</title>
        <style>
            body {{ font-family: 'Segoe UI'; background: #0f172a; color: white; text-align: center; padding: 50px; }}
            .card {{ background: #1e293b; padding: 20px; border-radius: 15px; display: inline-block; border: 1px solid #38bdf8; }}
            .price {{ color: #4ade80; font-size: 1.5em; font-weight: bold; }}
            .footer {{ margin-top: 20px; color: #94a3b8; font-size: 0.8em; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Master Quant Hub Dashboard 🔱</h1>
            <p>Status: <span style="color:#4ade80">● Monitoring Active</span></p>
            <hr border-color="#334155">
            <div style="text-align: left;">
                <p>Nifty 50: <span class="price">₹{prices['Nifty 50']}</span></p>
                <p>Reliance: <span class="price">₹{prices['Reliance']}</span></p>
                <p>HDFC Bank: <span class="price">₹{prices['HDFC Bank']}</span></p>
                <p>Gold (24K): <span class="price">₹{prices['Gold (10g)']}</span></p>
            </div>
            <div class="footer">
                Last Sync: {now} IST <br>
                Managed by Gemini Manager 🫡
            </div>
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✅ Dashboard updated with live market data!")

if __name__ == "__main__":
    prices = get_market_data()
    update_dashboard(prices)
