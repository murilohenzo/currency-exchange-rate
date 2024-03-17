from abc import ABC, abstractmethod
from typing import Optional, List

from domain.entities.Currency import Currency

class CurrencyRepository(ABC):
    @abstractmethod
    def get_by_code(self, code: str) -> Optional[Currency]:
        pass

    @abstractmethod
    def get_all(self) -> List[Currency]:
        pass