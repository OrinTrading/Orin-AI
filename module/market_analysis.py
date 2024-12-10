import random

class MarketAnalyzer:
    def fetch_market_data(self):
        print("Fetching market data...")
        return {"BTC": random.uniform(30000, 35000), "ETH": random.uniform(2000, 2500)}

    def analyze_opportunities(self, market_data):
        print("Analyzing market opportunities...")
        return {asset: price for asset, price in market_data.items() if price < 32000}

