class QuoteHistory:
    def __init__(self, timestamp, source_currency, target_currency, rate):
        self.timestamp = timestamp
        self.source_currency = source_currency
        self.target_currency = target_currency
        self.rate = rate