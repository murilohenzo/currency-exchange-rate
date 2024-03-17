from typing import List
from domain.entities.Currency import Currency
from domain.repositories.CurrencyRepository import CurrencyRepository

class CurrencyService:
    def __init__(self, currency_repository: CurrencyRepository):
        self.currency_repository = currency_repository

    def get_currency_by_code(self, code: str) -> Currency:
        return self.currency_repository.get_by_code(code)

    def get_all_currencies(self) -> List[Currency]:
        return self.currency_repository.get_all()