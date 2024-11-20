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

    def test_very_small_numbers(self):
        self.assertFalse(is_prime(-100))
        self.assertFalse(is_prime(-1000))

    def test_large_prime_numbers(self):
        self.assertTrue(is_prime(999983))  # A large prime number
        self.assertTrue(is_prime(982451653))  # Another large prime number

    def test_large_non_prime_numbers(self):
        self.assertFalse(is_prime(999984))  # Just one more than a large prime number
        self.assertFalse(is_prime(982451654))  # Just one more than another large prime number

    def test_even_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(1000000))

    def test_known_composite_numbers(self):
        self.assertFalse(is_prime(15))  # 3 * 5
        self.assertFalse(is_prime(21))  # 3 * 7
        self.assertFalse(is_prime(49))  # 7 * 7

    def test_known_prime_numbers(self):
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))

    def test_squares_of_primes(self):
        self.assertFalse(is_prime(4))  # 2^2
        self.assertFalse(is_prime(9))  # 3^2
        self.assertFalse(is_prime(25))  # 5^2

    def test_products_of_two_primes(self):
        self.assertFalse(is_prime(6))  # 2 * 3
        self.assertFalse(is_prime(15))  # 3 * 5
        self.assertFalse(is_prime(35))  # 5 * 7

if __name__ == '__main__':
    unittest.main()