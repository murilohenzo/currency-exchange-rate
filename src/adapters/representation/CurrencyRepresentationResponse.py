class CurrencyRepresentationResponse:
    def __init__(self, id: int, name: str, symbol: str):
        self.id = id
        self.name = name
        self.symbol = symbol
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'symbol': self.symbol
        }