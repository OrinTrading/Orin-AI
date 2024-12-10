from modules.trading_wallet import Wallet
from modules.market_analysis import MarketAnalyzer
from modules.trade_executor import TradeExecutor
from modules.profit_reinvestment import ProfitReinvestor
from modules.risk_management import RiskManager
from utils.logger import Logger

def main():
    Logger.log("Initializing Orin AI...")

    # Initialize wallet
    wallet = Wallet(initial_funds=1000)
    Logger.log(f"Wallet initialized with balance: ${wallet.balance}")

    # Analyze market
    analyzer = MarketAnalyzer()
    market_data = analyzer.fetch_market_data()
    opportunities = analyzer.analyze_opportunities(market_data)

    # Risk management
    risk_manager = RiskManager(wallet.balance)
    for asset, price in opportunities.items():
        if risk_manager.is_within_risk_limit(price):
            Logger.log(f"Asset {asset} within risk limit. Proceeding with trade.")

    # Execute trades
    executor = TradeExecutor(wallet)
    profits = executor.execute_trades(opportunities)

    # Reinvest profits
    reinvestor = ProfitReinvestor(wallet)
    reinvestor.reinvest(profits)
    Logger.log(f"Reinvestment complete. Final wallet balance: ${wallet.balance}")

if __name__ == "__main__":
    main()
