import unittest
import math
import Tasks.c1_fact as fact


class MyTestCase(unittest.TestCase):
    def test_fact_recursive(self):
        self.assertEqual(math.factorial(7), fact.factorial_recursive(7), msg="Something gonna wrong...")

    def test_fact_rec_exc(self):
        with self.assertRaises(ValueError, msg="ValueError should be here..."):
            fact.factorial_recursive(-11231)

    def test_fact_iterative(self):
        self.assertEqual(math.factorial(12), fact.factorial_iterative(12), msg="I think there's a mistake :)")

    def test_fact_iter_exc(self):
        with self.assertRaises(ValueError, msg="ValueError should be here..."):
            fact.factorial_iterative(-1121)


if __name__ == '__main__':
    unittest.main()
