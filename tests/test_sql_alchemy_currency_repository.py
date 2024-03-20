import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from pymysql import IntegrityError

from domain.entities.Currency import Currency
from infrastructure.repositories.SQLAlchemyCurrencyRepository import SQLAlchemyCurrencyRepository


class TestSQLAlchemyCurrencyRepository(unittest.TestCase):
    def setUp(self):
        self.mock_session = MagicMock(spec=Session)
        self.repo = SQLAlchemyCurrencyRepository(self.mock_session)

    def test_find_by_id(self):
        expected_currency = Currency(id=1, name='USD', symbol='$')

        self.mock_session.query.return_value.filter_by.return_value.first.return_value = expected_currency

        result = self.repo.find_by_id(1)

        self.assertEqual(result, expected_currency)

    def test_find_all(self):
        expected_currencies = [Currency(id=1, name='USD', symbol='$'), Currency(id=2, name='EUR', symbol='EUR')]

        self.mock_session.query.return_value.all.return_value = expected_currencies

        result = self.repo.find_all()

        self.assertEqual(result, expected_currencies)

    def test_create(self):
        currency = Currency(id=1, name='USD', symbol='$')

        self.mock_session.add.return_value = None
        self.mock_session.commit.return_value = None

        result = self.repo.create(currency)

        self.assertEqual(result, currency)

    def test_create_with_integrity_error(self):
    
        currency = Currency(id=1, name='USD', symbol='$')

        self.mock_session.add.side_effect = IntegrityError(MagicMock(), MagicMock(), MagicMock())
        
        result = self.repo.create(currency)

        self.assertIsNone(result)
        self.mock_session.rollback.assert_called_once()