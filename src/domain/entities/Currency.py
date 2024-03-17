from sqlalchemy import Column, Integer, String
from config.Database import Base

class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    code = Column(String(3), nullable=False)
    name = Column(String(100), nullable=False)
    symbol = Column(String(10), nullable=False)

    def __init__(self, id: int, code: str, name: str, symbol: str):
        self.id = id
        self.code = code
        self.name = name
        self.symbol = symbol