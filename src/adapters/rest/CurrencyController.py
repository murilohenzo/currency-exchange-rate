from flask import jsonify

class CurrencyController:
    def __init__(self, currency_service):
        self.currency_service = currency_service

    def get_all_currencies(self):
        currencies = self.currency_service.get_all_currencies()
        return jsonify(currencies)