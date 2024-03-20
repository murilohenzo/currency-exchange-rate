import unittest
from adapters.representation.CurrencyRepresentationRequest import CurrencyRepresentationRequest

class TestCurrencyRepresentationRequest(unittest.TestCase):
    def test_init(self):
        # Test data
        name = "USD"
        symbol = "$"

        # Criar uma instância de CurrencyRepresentationRequest
        request = CurrencyRepresentationRequest(name, symbol)

        # Verificar se os atributos são definidos corretamente
        self.assertEqual(request.name, name)
        self.assertEqual(request.symbol, symbol)

if __name__ == '__main__':
    unittest.main()
