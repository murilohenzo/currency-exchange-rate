import unittest
from unittest.mock import MagicMock
from domain.service.CurrencyService import CurrencyService, Currency, CurrencyRepository

class TestCurrencyService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock(spec=CurrencyRepository)
        self.currency_service = CurrencyService(self.mock_repository)

    def test_find_by_id(self):
        expected_currency = Currency(id=1, name="USD", symbol="$")
        self.mock_repository.find_by_id.return_value = expected_currency

        result = self.currency_service.find_by_id(1)

        self.assertEqual(result, expected_currency)
        self.mock_repository.find_by_id.assert_called_once_with(1)

    def test_find_all(self):
        expected_currencies = [
            Currency(id=1, name="USD", symbol="$"),
            Currency(id=2, name="EUR", symbol="€")
        ]
        self.mock_repository.find_all.return_value = expected_currencies

        result = self.currency_service.find_all()

        self.assertEqual(result, expected_currencies)
        self.mock_repository.find_all.assert_called_once()

    def test_create(self):
        new_currency = Currency(id=None, name="GBP", symbol="£")
        self.mock_repository.create.return_value = new_currency

        result = self.currency_service.create(new_currency)

        self.assertEqual(result, new_currency)
        self.mock_repository.create.assert_called_once_with(new_currency)

if __name__ == '__main__':
    unittest.main()
