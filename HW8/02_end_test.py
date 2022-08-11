import unittest
from unittest import mock
from Goldbachs import even, eratosthenes, goldbach, odd_primes, CustomError

@mock.patch('builtins.input')  
class gbtest(unittest.TestCase):
    def test_goldbach(self, mock_input):
        mock_input.return_value=8
        gb=goldbach()
        self.assertEqual(gb, (3,5))
        
if __name__ == "__main__":
    unittest.main()