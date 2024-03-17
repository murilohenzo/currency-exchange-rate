from abc import ABC, abstractmethod

class ExchangeRateRepository(ABC):
    @abstractmethod
    def get_exchange_rate(self, source_currency_code, target_currency_code):
        pass

    @abstractmethod
    def save_exchange_rate(self, exchange_rate):
        pass