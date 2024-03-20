import unittest
from src.utils.Monad import Maybe


class TestMaybe(unittest.TestCase):
  def test_bind_with_value(self):
    maybe = Maybe(5)
    result = maybe.bind(lambda x: x * 2)

    self.assertEqual(result.value, 10)

  def test_bind_with_none_value(self):
    maybe = Maybe(None)
    result = maybe.bind(lambda x: x * 2)

    self.assertIsNone(result.value)

  def test_bind_chaining(self):
    maybe = Maybe(5)
    result = maybe.bind(lambda x: x * 2).bind(lambda x: x + 3)

    self.assertEqual(result.value, 13)


if __name__ == '__main__':
  unittest.main()
