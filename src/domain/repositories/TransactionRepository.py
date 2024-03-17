from abc import ABC, abstractmethod

class TransactionRepository(ABC):
    @abstractmethod
    def save_transaction(self, transaction):
        pass

    @abstractmethod
    def get_transactions(self, start_date, end_date):
        pass