import unittest
from src.adapters.representation.CurrencyRepresentationResponse import CurrencyRepresentationResponse

class TestCurrencyRepresentationResponse(unittest.TestCase):
    def test_init(self):
        # Test data
        id = 1
        name = "USD"
        symbol = "$"

        # Criar uma instância de CurrencyRepresentationResponse
        response = CurrencyRepresentationResponse(id, name, symbol)

        # Verificar se os atributos são definidos corretamente
        self.assertEqual(response.id, id)
        self.assertEqual(response.name, name)
        self.assertEqual(response.symbol, symbol)

    def test_to_dict(self):
        # Test data
        id = 1
        name = "USD"
        symbol = "$"

        # Criar uma instância de CurrencyRepresentationResponse
        response = CurrencyRepresentationResponse(id, name, symbol)

        # Chamar o método to_dict()
        result = response.to_dict()

        # Verificar se o dicionário retornado está correto
        expected_dict = {'id': id, 'name': name, 'symbol': symbol}
        self.assertEqual(result, expected_dict)

if __name__ == '__main__':
    unittest.main()
