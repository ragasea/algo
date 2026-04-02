def update_dashboard(prices):
    now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
    
    # We embed the CSS and JavaScript directly into the string
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Master Quant Hub 🔱</title>
        <style>
            body {{ font-family: 'Segoe UI'; background: #0f172a; color: white; text-align: center; padding: 50px; }}
            .card {{ background: #1e293b; padding: 30px; border-radius: 15px; display: inline-block; border: 1px solid #38bdf8; min-width: 300px; }}
            .price {{ color: #4ade80; font-size: 1.5em; font-weight: bold; display: block; margin-bottom: 10px; }}
            button {{ background: #38bdf8; color: #0f172a; border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; cursor: pointer; margin-top: 20px; }}
            .footer {{ margin-top: 20px; color: #94a3b8; font-size: 0.8em; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Master Quant Hub 🔱</h1>
            <p>Nifty 50: <span class="price">₹{prices['Nifty 50']}</span></p>
            <p>Reliance: <span class="price">₹{prices['Reliance']}</span></p>
            
            <button onclick="window.location.reload()">🔄 Refresh Prices</button>
            
            <div class="footer">
                Last System Sync: {now} IST <br>
                Managed by Gemini Manager 🫡
            </div>
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✅ Dashboard updated with Refresh Button logic!")
