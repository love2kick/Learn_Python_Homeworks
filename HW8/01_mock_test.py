import unittest
from unittest import mock
from Goldbachs import (even, eratosthenes, goldbach, 
                       odd_primes, CustomError)

class gbtest(unittest.TestCase):
    def test_even(self):
        ev=even(8)
        self.assertEqual(ev, (True, 8))
        
    @mock.patch('builtins.input')    
    def test_even_word(self, mock_input):
        mock_input.return_value="asd"
        with self.assertRaises(ValueError):
            even('asd')
        
    @mock.patch('builtins.input')    
    def test_even_noteven(self, mock_input):
        mock_input.return_value=7
        with self.assertRaises(CustomError):
            even(9)
            
    @mock.patch('builtins.input')    
    def test_even_toosmall(self, mock_input):
        mock_input.return_value=2
        with self.assertRaises(CustomError):
            even(2)
        
    def test_eratosphenes(self):
        er=eratosthenes(8)
        self.assertEqual(er, [2, 3, 5, 7])
        
    @mock.patch('Goldbachs.eratosthenes')
    def test_oddprimes(self, mock_eratosthenes):
        mock_eratosthenes.return_value=[2, 3, 5, 7]
        op=odd_primes(8)
        self.assertEqual(op, [3, 5, 7])
        
    @mock.patch('os.system')
    @mock.patch('builtins.input')  
    @mock.patch('Goldbachs.even')    
    @mock.patch('Goldbachs.odd_primes')
    def test_goldbach(self, mock_oddprimes , mock_even, mock_input, os):
        mock_input.return_value=8
        mock_even.return_value=True, 8
        mock_oddprimes.return_value=[3, 5, 7]
        gb=goldbach()
        self.assertEqual(gb, (3,5))
        
if __name__ == "__main__":
    unittest.main()