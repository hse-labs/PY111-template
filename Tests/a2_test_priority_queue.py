import unittest
import Tasks.a2_priority_queue as priority_queue


class MyTestCase(unittest.TestCase):
	def setUp(self):
		priority_queue.clear()

	def test_clear(self):
		priority_queue.enqueue(3)
		priority_queue.clear()

		self.assertIsNone(priority_queue.dequeue())

	def test_enqueue_dequeue_without_priority(self):
		initial_elem = 3
		priority_queue.enqueue(initial_elem)

		self.assertEqual(initial_elem, priority_queue.dequeue())

	def test_multiple_en_de_queues_without_priority(self):
		items = [i for i in range(10)]

		for i in items:
			priority_queue.enqueue(i)

		received_items = []
		for _ in items:
			received_items.append(priority_queue.dequeue())

		self.assertEqual(items, received_items)

	def test_peek(self):
		priority_queue.enqueue(3)
		priority_queue.enqueue(5)

		self.assertEqual(3, priority_queue.peek())
		self.assertEqual(5, priority_queue.peek(1))
		self.assertEqual(3, priority_queue.peek())

	def test_en_de_queue_with_priority(self):
		priority_queue.enqueue(0, 1)
		priority_queue.enqueue(10, 0)

		self.assertEqual(10, priority_queue.dequeue())


if __name__ == '__main__':
	unittest.main()
