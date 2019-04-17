import unittest
import math
import Tasks.c1_fact as fact


class MyTestCase(unittest.TestCase):
	def test_fact_recursive(self):
		self.assertEqual(fact.factorial_recursive(7), math.factorial(7), msg="Something gonna wrong...")

	def test_fact_rec_exc(self):
		with self.assertRaises(ValueError, msg="ValueError should be here..."):
			fact.factorial_recursive(-11231)

	def test_fact_iterative(self):
		self.assertEqual(fact.factorial_iterative(12), math.factorial(12), msg="I think it's a mistake :)")

	def test_fact_iter_exc(self):
		with self.assertRaises(ValueError, msg="ValueError should be here..."):
			fact.factorial_recursive(-1121)


if __name__ == '__main__':
	unittest.main()
