import unittest
import Tasks.a1_my_queue as my_queue


class MyTestCase(unittest.TestCase):
	def setUp(self):
		my_queue.clear()

	def test_clear(self):
		my_queue.enqueue(3)
		my_queue.clear()

		self.assertIsNone(my_queue.dequeue())

	def test_enqueue_dequeue(self):
		initial_elem = 3
		my_queue.enqueue(initial_elem)

		self.assertEqual(initial_elem, my_queue.dequeue())

	def test_multiple_en_de_queues(self):
		items = [i for i in range(10)]

		for i in items:
			my_queue.enqueue(i)

		received_items = []
		for _ in items:
			received_items.append(my_queue.dequeue())

		self.assertEqual(items, received_items)

	def test_peek(self):
		my_queue.enqueue(3)
		my_queue.enqueue(5)

		self.assertEqual(3, my_queue.peek())
		self.assertEqual(5, my_queue.peek(1))
		self.assertEqual(3, my_queue.peek())


if __name__ == '__main__':
	unittest.main()
