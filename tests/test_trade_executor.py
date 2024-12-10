import unittest
from modules.trade_executor import TradeExecutor
from modules.trading_wallet import Wallet

class TestTradeExecutor(unittest.TestCase):
    def test_execute_trades(self):
        wallet = Wallet(1000)
        executor = TradeExecutor(wallet)
        opportunities = {"BTC": 31000}
        profits = executor.execute_trades(opportunities)
        self.assertGreater(profits, 0)
        self.assertLess(wallet.balance, 1000)

if __name__ == "__main__":
    unittest.main()

