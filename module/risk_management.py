class RiskManager:
    def __init__(self, balance, risk_tolerance=0.1):
        self.balance = balance
        self.risk_tolerance = risk_tolerance

    def calculate_max_risk(self):
        return self.balance * self.risk_tolerance

    def is_within_risk_limit(self, trade_amount):
        return trade_amount <= self.calculate_max_risk()
