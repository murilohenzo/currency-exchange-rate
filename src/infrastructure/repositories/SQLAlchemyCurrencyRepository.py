from sqlalchemy.orm import Session
from typing import Optional, List
from domain.entities.Currency import Currency
from domain.repositories.CurrencyRepository import CurrencyRepository

class SQLAlchemyCurrencyRepository(CurrencyRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_code(self, code: str) -> Optional[Currency]:
        return self.session.query(Currency).filter_by(code=code).first()

    def get_all(self) -> List[Currency]:
        return self.session.query(Currency).all()