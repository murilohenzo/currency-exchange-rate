import unittest
from unittest.mock import MagicMock
from flask import Flask

from domain.entities.Currency import Currency
from mappers.CurrencyMapper import CurrencyMapper
from adapters.representation.CurrencyRepresentationResponse import CurrencyRepresentationResponse
from adapters.rest.CurrencyController import CurrencyController

class TestCurrencyController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.currency_service_mock = MagicMock()
        self.controller = CurrencyController(self.currency_service_mock)
        self.app.add_url_rule('/create', 'create', self.controller.create, methods=['POST'])

    def test_find_by_id(self):
        currency_id = 1
        currency_data = Currency(id=currency_id, name='USD', symbol='$')
        self.currency_service_mock.find_by_id.return_value = currency_data

        with self.app.test_request_context():
            response, _ = self.controller.find_by_id(currency_id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["id"], currency_id)
        self.assertIsNotNone(response.json)

    def test_find_all(self):
        currencies = [Currency(id=1, name='USD', symbol='$'), Currency(id=2, name='EUR', symbol='€')]
        self.currency_service_mock.find_all.return_value = currencies

        with self.app.test_request_context():
            response = self.controller.find_all()
        
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)

    def test_find_by_name(self):
        currency_name = 'USD'
        currencies = [Currency(id=1, name='USD', symbol='$'), Currency(id=2, name='EUR', symbol='€')]
        self.currency_service_mock.find_all.return_value = currencies

        with self.app.test_request_context():
            response = self.controller.find_by_name(currency_name)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]["name"], currency_name)


    def test_create_with_error(self):
        request_data = {'name': 'USD', 'symbol': '$'}
        created_currency = {'id': 1, 'name': 'USD', 'symbol': '$'}
        mapped_entity = MagicMock()
        mapped_response = CurrencyRepresentationResponse(**created_currency)
        self.currency_service_mock.create.return_value = created_currency
        CurrencyMapper.map_request_to_entity.return_value = mapped_entity
        CurrencyMapper.map_entity_to_response.return_value = mapped_response
        
        with self.app.test_client() as client:
          response = client.post('/currencies', json=request_data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()