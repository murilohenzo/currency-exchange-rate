import unittest
from src.adapters.representation.CurrencyRepresentationRequest import CurrencyRepresentationRequest

class TestCurrencyRepresentationRequest(unittest.TestCase):
    def test_init(self):
        name = "USD"
        symbol = "$"

        request = CurrencyRepresentationRequest(name, symbol)

        self.assertEqual(request.name, name)
        self.assertEqual(request.symbol, symbol)

if __name__ == '__main__':
    unittest.main()
