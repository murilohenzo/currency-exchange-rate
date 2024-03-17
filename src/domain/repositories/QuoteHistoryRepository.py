from abc import ABC, abstractmethod

class QuoteHistoryRepository(ABC):
    @abstractmethod
    def save_quote(self, quote_history):
        pass

    @abstractmethod
    def get_quotes_by_currency(self, currency_code):
        pass