import unittest

import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from gcd import gcd

class TestGSD(unittest.TestCase):

	def test_first_value_is_0(self):
		self.assertEqual(gcd(0, 5), 5)

	def test_second_value_is_0(self):
		self.assertEqual(gcd(3, 0), 3)

	def test_first_value_is_1(self):
		self.assertEqual(gcd(1, 126), 1)

	def test_second_value_is_1(self):
		self.assertEqual(gcd(534, 1), 1)

	def test_equal_values(self):
		self.assertEqual(gcd(344235, 344235), 344235)

	def test_first_value_is_even_second_value_is_odd(self):
		self.assertEqual(gcd(10, 5), 5)

	def test_first_value_is_odd_second_value_is_even(self):
		self.assertEqual(gcd(5, 10), 5)

	def test_values_is_even(self):
		self.assertEqual(gcd(64, 1024), 64)

	def test_values_is_odd(self):
		self.assertEqual(gcd(3, 9), 3)

if __name__ == '__main__':
	unittest.main()