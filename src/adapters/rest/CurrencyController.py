from flask import abort, jsonify, request
from domain.service.Monad import Maybe
from adapters.representation.CurrencyRepresentationResponse import CurrencyRepresentationResponse
from mappers.CurrencyMapper import CurrencyMapper

class CurrencyController:
    def __init__(self, currency_service):
        self.currency_service = currency_service

    def find_by_id(self, id):
        currency = self.currency_service.find_by_id(id)
        #uso de Monad
        maybe_currency = Maybe(currency)
        #uso de funções lambda juntamente com o monad
        return maybe_currency.bind(lambda currency: CurrencyMapper.map_entity_to_response(currency)
                                   .to_dict()) \
                                   .bind(lambda response_dict: jsonify(response_dict))\
                                   .value or jsonify({"error": "Currency not found"}),404          
    
    def find_all(self):
      
      currencies = self.currency_service.find_all()
      currency_responses = [CurrencyRepresentationResponse(
          id=currency.id,
          name=currency.name,
          symbol=currency.symbol
      ).to_dict() for currency in currencies]
      return jsonify(currency_responses)
    
    def find_by_name(self, name):
        #Closure para retornar moedas com o nome selecionado
        def get_currencies_by_name(currency):
            return currency.name == name
        currency = self.currency_service.find_all()
        filtered_currencies = currency.filter(get_currencies_by_name, currency)
        currency_responses = [CurrencyRepresentationResponse(
            id=currency.id,
            name=currency.name,
            symbol=currency.symbol
        ).to_dict() for currency in filtered_currencies]
        return jsonify(currency_responses)
    
    def create(self):
        data = request.json
        currency_request = CurrencyRepresentationResponse(**data)
        currency = CurrencyMapper.map_request_to_entity(currency_request)
        created_currency = self.currency_service.create(currency)
        response = CurrencyMapper.map_entity_to_response(created_currency)
        return jsonify(response.to_dict())
    