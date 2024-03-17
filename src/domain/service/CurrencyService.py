from typing import List
from domain.entities.Currency import Currency
from domain.repositories.CurrencyRepository import CurrencyRepository

class CurrencyService:
    def __init__(self, currency_repository: CurrencyRepository):
        self.currency_repository = currency_repository

    def find_by_id(self, id: int) -> Currency:
        currency = self.currency_repository.find_by_id(id)
        return currency

    def find_all(self) -> List[Currency]:
        currencies = self.currency_repository.find_all()
        return currencies
    
    def create(self, currency: Currency) -> Currency:
        return self.currency_repository.create(currency)