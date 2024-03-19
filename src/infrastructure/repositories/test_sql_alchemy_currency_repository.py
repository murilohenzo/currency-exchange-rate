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
        # Mocking data
        expected_currency = Currency(id=1, name='USD', symbol='$')

        # Mocking session.query().filter_by().first() method
        self.mock_session.query.return_value.filter_by.return_value.first.return_value = expected_currency

        # Test
        result = self.repo.find_by_id(1)

        # Assertion
        self.assertEqual(result, expected_currency)

    def test_find_all(self):
        # Mocking data
        expected_currencies = [Currency(id=1, name='USD', symbol='$'), Currency(id=2, name='EUR', symbol='EUR')]

        # Mocking session.query().all() method
        self.mock_session.query.return_value.all.return_value = expected_currencies

        # Test
        result = self.repo.find_all()

        # Assertion
        self.assertEqual(result, expected_currencies)

    def test_create(self):
        # Mocking data
        currency = Currency(id=1, name='USD', symbol='$')

        # Mocking session.add() and session.commit() methods
        self.mock_session.add.return_value = None
        self.mock_session.commit.return_value = None

        # Test
        result = self.repo.create(currency)

        # Assertion
        self.assertEqual(result, currency)

    def test_create_with_integrity_error(self):
        # Mocking data
        currency = Currency(id=1, name='USD', symbol='$')

        # Mocking session.add() and session.commit() methods to raise IntegrityError
        self.mock_session.add.side_effect = IntegrityError(MagicMock(), MagicMock(), MagicMock())
        
        result = self.repo.create(currency)

        # Assertion
        self.assertIsNone(result)
        self.mock_session.rollback.assert_called_once()