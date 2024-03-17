from abc import ABC, abstractmethod
from typing import Optional, List

from domain.entities.Currency import Currency

class CurrencyRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Currency]:
        pass

    @abstractmethod
    def find_all(self) -> List[Currency]:
        pass
    
    @abstractmethod
    def create(self, currency: Currency) -> Currency:
        pass