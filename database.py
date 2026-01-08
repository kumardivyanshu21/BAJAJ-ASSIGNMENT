class MockDatabase:
    def __init__(self):
        self.instruments = [
            {"symbol": "BAJAJ-AUTO", "exchange": "NSE", "instrumentType": "EQUITY", "lastTradedPrice": 4500.0},
            {"symbol": "TATA-MOTORS", "exchange": "NSE", "instrumentType": "EQUITY", "lastTradedPrice": 900.0},
            {"symbol": "RELIANCE", "exchange": "NSE", "instrumentType": "EQUITY", "lastTradedPrice": 2400.0},
        ]
        
        self.orders = {} 
        self.trades = []
        self.portfolio = {}

db = MockDatabase()