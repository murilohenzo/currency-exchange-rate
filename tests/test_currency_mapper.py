import unittest
from src.mappers.CurrencyMapper import CurrencyMapper, CurrencyRepresentationRequest, CurrencyRepresentationResponse, Currency

class TestCurrencyMapper(unittest.TestCase):
    def test_map_request_to_entity(self):
        request_data = CurrencyRepresentationRequest(name="USD", symbol="$")

        result = CurrencyMapper.map_request_to_entity(request_data)

        self.assertEqual(result.id, None)
        self.assertEqual(result.name, "USD")
        self.assertEqual(result.symbol, "$")

    def test_map_entity_to_response(self):
        currency = Currency(id=1, name="USD", symbol="$")

        result = CurrencyMapper.map_entity_to_response(currency)

        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, "USD")
        self.assertEqual(result.symbol, "$")

if __name__ == '__main__':
    unittest.main()
