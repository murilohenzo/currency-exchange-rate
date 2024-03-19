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
    self.register_currency_controller()

  def configure_app(self):
    self.app.config.from_object(AppConfig)

  def register_currency_controller(self):
    currency_controller = CurrencyController(self.container.get_currency_service())
    self.app.add_url_rule('/currencies/<int:id>', 'find_by_id', currency_controller.find_by_id, methods=['GET'])
    self.app.add_url_rule('/currencies/<string:name>', 'find_by_name', currency_controller.find_by_name,
                          methods=['GET'])
    self.app.add_url_rule('/currencies', 'find_all', currency_controller.find_all, methods=['GET'])
    self.app.add_url_rule('/currencies', 'create', currency_controller.create, methods=['POST'])

  def run(self):
    self.app.run(host='0.0.0.0', port='8080')


if __name__ == "__main__":
  main = Application()
  main.run()
