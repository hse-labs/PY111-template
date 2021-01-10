import unittest
import Tasks.c0_fib as fib


class MyTestCase(unittest.TestCase):
    def test_fib_recursive(self):
        self.assertEqual(21, fib.fib_recursive(8),
                         msg="Something wrong. Do you remember that Fibonacci sequence start from 0?..")

    def test_fib_exc(self):
        with self.assertRaises(ValueError,
                               msg="Is there a -35 number of Fibonacci sequence? I think here should be an exception..."):
            fib.fib_recursive(-35)

    def test_fib_iterative(self):
        self.assertEqual(34, fib.fib_iterative(9),
                         msg="Something wrong. Do you remember that Fibonacci sequence start from 0?..")

    def test_fib_iter_exc(self):
        with self.assertRaises(ValueError,
                               msg="Is there a -1 number of Fibonacci sequence? I think here should be and exception..."):
            fib.fib_iterative(-1)


if __name__ == '__main__':
    unittest.main()
