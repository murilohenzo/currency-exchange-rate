from adapters.representation.CurrencyRepresentationRequest import CurrencyRepresentationRequest
from adapters.representation.CurrencyRepresentationResponse import CurrencyRepresentationResponse
from domain.entities.Currency import Currency

class CurrencyMapper:
    @staticmethod
    def map_request_to_entity(request_data: CurrencyRepresentationRequest) -> Currency:
        return Currency(
            id=None,
            name=request_data.name,
            symbol=request_data.symbol
        )

    @staticmethod
    def map_entity_to_response(currency: Currency) -> CurrencyRepresentationResponse:
        return CurrencyRepresentationResponse(
            id=currency.id,
            name=currency.name,
            symbol=currency.symbol
        )
