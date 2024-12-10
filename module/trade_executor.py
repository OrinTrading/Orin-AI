class TradeExecutor:
    def __init__(self, wallet):
        self.wallet = wallet

    def execute_trades(self, opportunities):
        print("Executing trades...")
        total_profit = 0
        for asset, price in opportunities.items():
            profit = price * 0.05
            total_profit += profit
            self.wallet.withdraw(100)
            print(f"Trade executed for {asset}. Profit: ${profit:.2f}")
        return total_profit

