#Prime number test cases.

import unittest
from prime import prime

class TestPrime(unittest.TestCase):
	
	# Test if function correctly returns prime numbers. 
	def test_prime(self):
		self.assertEqual(prime.prime(10), [2, 3, 5, 7])

# Test if function correctly returns prime numbers. 
	def test_prime(self):
		self.assertEqual(prime.prime(20), [2, 3, 5, 7, 11, 13, 17, 19])

# Test if function correctly returns prime numbers. 
	def test_prime(self):
		self.assertEqual(prime.prime(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

# Test if function correctly returns prime numbers. 
	def test_prime(self):
		self.assertEqual(prime.prime(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

# Test if function returns there are o prime numbers if number less than 0 entered.
	def test_less_than_zero(self):
		self.assertEqual(prime.prime(0))

# Test if function returns there are o prime numbers if 1 is entered.
	def test_one(self):
		self.assertEqual(prime.prime(1))	


	# Test if function returns an error message if wrong data type passed to function.
	def test_invalid_type(self):
		self.assertEqual(prime.prime("String"))
 