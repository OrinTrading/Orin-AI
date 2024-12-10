import unittest
from modules.market_analysis import MarketAnalyzer

class TestMarketAnalyzer(unittest.TestCase):
    def test_analyze_opportunities(self):
        analyzer = MarketAnalyzer()
        market_data = {"BTC": 31000, "ETH": 3500}
        opportunities = analyzer.analyze_opportunities(market_data)
        self.assertIn("BTC", opportunities)
        self.assertNotIn("ETH", opportunities)

if __name__ == "__main__":
    unittest.main()

