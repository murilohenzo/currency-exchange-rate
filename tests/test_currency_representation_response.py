import unittest
from src.adapters.representation.CurrencyRepresentationResponse import CurrencyRepresentationResponse

class TestCurrencyRepresentationResponse(unittest.TestCase):
    def test_init(self):
        id = 1
        name = "USD"
        symbol = "$"

        response = CurrencyRepresentationResponse(id, name, symbol)

        self.assertEqual(response.id, id)
        self.assertEqual(response.name, name)
        self.assertEqual(response.symbol, symbol)

    def test_to_dict(self):
        id = 1
        name = "USD"
        symbol = "$"

        response = CurrencyRepresentationResponse(id, name, symbol)

        result = response.to_dict()

        expected_dict = {'id': id, 'name': name, 'symbol': symbol}
        self.assertEqual(result, expected_dict)

if __name__ == '__main__':
    unittest.main()
