import unittest
import Tasks.a0_my_stack as my_stack


class MyTestCase(unittest.TestCase):
    def setUp(self):
        my_stack.clear()

    def test_clear(self):
        my_stack.push(3)
        my_stack.clear()

        self.assertIsNone(my_stack.pop(), msg="Did you clear the stack?")

    def test_empty_stack(self):
        self.assertIsNone(my_stack.pop(), msg="Should return None if no elements")

    def test_push_pop(self):
        initial_elem = 3
        my_stack.push(initial_elem)

        self.assertEqual(initial_elem, my_stack.pop())

    def test_multiple_pushes_pops(self):
        items = [i for i in range(10)]

        for i in items:
            my_stack.push(i)

        received_items = []
        for _ in items:
            received_items.append(my_stack.pop())

        self.assertEqual(list(reversed(items)), received_items)

    def test_peek(self):
        my_stack.push(7)
        my_stack.push(3)
        my_stack.push(5)

        self.assertEqual(5, my_stack.peek())
        self.assertEqual(3, my_stack.peek(1))
        self.assertEqual(5, my_stack.peek())

        self.assertIsNone(my_stack.peek(100), msg="Should return None if no elements")


if __name__ == '__main__':
    unittest.main()
