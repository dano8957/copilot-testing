import unittest
from prime import is_prime  # Assuming the function is_prime is defined in prime.py

class TestPrime(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-10))
        self.assertFalse(is_prime(-17))

    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

    def test_small_primes(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_small_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

    def test_large_primes(self):
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(37))

    def test_large_non_primes(self):
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(27))
        self.assertFalse(is_prime(35))

    def test_very_large_numbers(self):
        self.assertTrue(is_prime(104729))  # 10000th prime number
        self.assertFalse(is_prime(104728))  # Just one less than 10000th prime number

if __name__ == '__main__':
    unittest.main()