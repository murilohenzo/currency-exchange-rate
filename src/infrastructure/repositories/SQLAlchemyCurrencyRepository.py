from pymysql import IntegrityError
from sqlalchemy.orm import Session
from typing import Optional, List
from domain.entities.Currency import Currency
from domain.repositories.CurrencyRepository import CurrencyRepository


class SQLAlchemyCurrencyRepository(CurrencyRepository):
  def __init__(self, session: Session):
    self.session = session

  def find_by_id(self, id: int) -> Optional[Currency]:
    return self.session.query(Currency).filter_by(id=id).first()

  def find_all(self) -> List[Currency]:
    return self.session.query(Currency).all()

  def create(self, currency: Currency) -> Currency:
    try:
      self.session.add(currency)
      self.session.commit()
      return currency
    except IntegrityError as e:
      print(f"[E23] - CurrencyViolationError: {e}")
      self.session.rollback()
