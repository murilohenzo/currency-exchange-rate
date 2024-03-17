from flask import abort, jsonify, request

from adapters.representation.CurrencyRepresentationResponse import CurrencyRepresentationResponse
from mappers.CurrencyMapper import CurrencyMapper

class CurrencyController:
    def __init__(self, currency_service):
        self.currency_service = currency_service

    def find_by_id(self, id):
        currency = self.currency_service.find_by_id(id)
        if currency is None:
            response = jsonify({"error": "Currency not found"})
            response.status_code = 404
            return response
        response = CurrencyMapper.map_entity_to_response(currency)
        return jsonify(response.to_dict())

    def find_all(self):
      currencies = self.currency_service.find_all()
      currency_responses = [CurrencyRepresentationResponse(
          id=currency.id,
          name=currency.name,
          symbol=currency.symbol
      ).to_dict() for currency in currencies]
      return jsonify(currency_responses)
    
    def create(self):
        data = request.json
        currency_request = CurrencyRepresentationResponse(**data)
        currency = CurrencyMapper.map_request_to_entity(currency_request)
        created_currency = self.currency_service.create(currency)
        response = CurrencyMapper.map_entity_to_response(created_currency)
        return jsonify(response.to_dict())