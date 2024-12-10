class ProfitReinvestor:
    def __init__(self, wallet):
        self.wallet = wallet

    def reinvest(self, profits):
        print("Reinvesting profits...")
        self.wallet.deposit(profits)
        print(f"${profits:.2f} reinvested into wallet.")
