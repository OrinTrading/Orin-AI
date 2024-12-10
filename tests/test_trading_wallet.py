import unittest
from modules.trading_wallet import Wallet

class TestWallet(unittest.TestCase):
    def test_deposit(self):
        wallet = Wallet(100)
        wallet.deposit(50)
        self.assertEqual(wallet.balance, 150)

    def test_withdraw(self):
        wallet = Wallet(100)
        withdrawn = wallet.withdraw(50)
        self.assertEqual(wallet.balance, 50)
        self.assertEqual(withdrawn, 50)

if __name__ == "__main__":
    unittest.main()

