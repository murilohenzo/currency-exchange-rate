from config.Database import Database
from domain.service.CurrencyService import CurrencyService
from infrastructure.repositories.SQLAlchemyCurrencyRepository import SQLAlchemyCurrencyRepository


class DependencyContainer:
    """
    DependencyContainer class manages dependencies within the application.
    It initializes the database, creates necessary tables, and provides instances of services to other components.
    """

    def __init__(self):
        """
        Initializes the DependencyContainer.

        Attributes:
            database (Database): An instance of the Database class responsible for database management.
            currency_repository (SQLAlchemyCurrencyRepository): An instance of the SQLAlchemyCurrencyRepository class
                responsible for handling currency data persistence using SQLAlchemy.
            currency_service (CurrencyService): An instance of the CurrencyService class responsible for implementing
                business logic related to currencies.
        """
        self.database = Database()
        self.database.create_tables()
        self.currency_repository = SQLAlchemyCurrencyRepository(self.database.get_session())
        self.currency_service = CurrencyService(self.currency_repository)

    def get_currency_service(self):
        """
        Returns the currency_service instance, allowing other components to access the currency-related functionalities.

        Returns:
            CurrencyService: An instance of the CurrencyService class.
        """
        return self.currency_service
