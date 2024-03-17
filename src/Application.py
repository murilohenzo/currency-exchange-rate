from flask import Flask
from adapters.rest.CurrencyController import CurrencyController
from config.DependencyContainer import DependencyContainer

class AppConfig:
    DEBUG = False

class Application:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.container = DependencyContainer()
        self.register_controllers()
    
    def configure_app(self):
        self.app.config.from_object(AppConfig)

    def register_controllers(self):
        currency_controller = CurrencyController(self.container.get_currency_service())
        self.app.add_url_rule('/currencies', 'get_all_currencies', currency_controller.get_all_currencies, methods=['GET'])
    
    def run(self):
        self.app.run(host='0.0.0.0', port='8080')


if __name__ == "__main__":
    main = Application()
    main.run()
