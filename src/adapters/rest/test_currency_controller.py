import unittest
from unittest.mock import MagicMock
from flask import Flask, jsonify
from adapters.rest.CurrencyController import CurrencyController 
from adapters.representation.CurrencyRepresentationResponse import CurrencyRepresentationResponse
from adapters.representation.CurrencyRepresentationRequest import CurrencyRepresentationRequest
from adapters.representation.CurrencyRepresentationRequest import CurrencyRepresentationRequest
from mappers.CurrencyMapper import CurrencyMapper

class TestCurrencyController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.currency_service_mock = MagicMock()
        self.controller = CurrencyController(self.currency_service_mock)
        self.app.add_url_rule('/create', 'create', self.controller.create, methods=['POST'])

    def test_find_by_id(self):
        currency_id = 1
        currency_data = {'id': currency_id, 'name': 'USD', 'symbol': '$'}
        self.currency_service_mock.find_by_id.return_value = currency_data

        with self.app.test_request_context():
            response, status_code = self.controller.find_by_id(currency_id)

        self.assertEqual(status_code, 404)
        self.assertEqual(response.json, currency_data)

    def test_find_all(self):
        currencies = [{'id': 1, 'name': 'USD', 'symbol': '$'}, {'id': 2, 'name': 'EUR', 'symbol': '€'}]
        self.currency_service_mock.find_all.return_value = currencies

        with self.app.test_request_context():
            response = self.controller.find_all()

        self.assertEqual(response.json, currencies)

    def test_find_by_name(self):
        currency_name = 'USD'
        currencies_with_name = [{'id': 1, 'name': 'USD', 'symbol': '$'}, {'id': 2, 'name': 'USD', 'symbol': '€'}]
        self.currency_service_mock.find_all.return_value = currencies_with_name

        with self.app.test_request_context():
            response = self.controller.find_by_name(currency_name)

        self.assertEqual(response.json, currencies_with_name)

    def test_create(self):
        request_data = {'name': 'USD', 'symbol': '$'}
        created_currency = {'id': 1, 'name': 'USD', 'symbol': '$'}
        mapped_entity = MagicMock()
        mapped_response = CurrencyRepresentationResponse(**created_currency)
        self.currency_service_mock.create.return_value = created_currency
        CurrencyMapper.map_request_to_entity.return_value = mapped_entity
        CurrencyMapper.map_entity_to_response.return_value = mapped_response

        with self.app.test_client() as client:
            response = client.post('/create', json=request_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, created_currency)

if __name__ == '__main__':
    unittest.main()