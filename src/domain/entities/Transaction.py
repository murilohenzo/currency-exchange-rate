class Transaction:
    def __init__(self, timestamp, source_currency, target_currency, amount_original, amount_converted):
        self.timestamp = timestamp
        self.source_currency = source_currency
        self.target_currency = target_currency
        self.amount_original = amount_original
        self.amount_converted = amount_converted