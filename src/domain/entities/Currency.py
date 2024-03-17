from sqlalchemy import Column, Integer, String

from domain.entities.Base import Base

class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)
    symbol = Column(String(10), nullable=False)

    def __init__(self, id: int, name: str, symbol: str):
        self.id = id
        self.name = name
        self.symbol = symbol