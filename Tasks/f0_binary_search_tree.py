from typing import Any
# import networkx as nx
tree = {}
head_node = None


def req_ins(k, v, hn):
	global tree
	if k < hn and tree[hn][1] is None:
		tree[k] = [v, None, None]
		tree[hn][1] = k
	elif k > hn and tree[hn][2] is None:
		tree[k] = [v, None, None]
		tree[hn][2] = k
	elif hn > k != tree[hn][1] and tree[hn][1] is not None:
		req_ins(k, v, tree[hn][1])
	elif hn < k != tree[hn][1] and tree[hn][1] is not None:
		req_ins(k, v, tree[hn][2])
	else:
		return None



def insert(key: Any, value: Any) -> None:
	"""
	Insert (key, value) pair to binary search tree

	:param key: key from pair (key is used for positioning node in the tree)
	:param value: value associated with key
	:return: None
	"""
	global tree
	global head_node

	if not tree:
		head_node = key
		tree[key] = [value, None, None]
	elif key == head_node:
		tree[key] = [value, None, None]
	else:
		req_ins(key, value, head_node)
	return None


def remove(key: Any) -> (Any, Any):
	"""
	Remove key and associated value from the BST

	:param key: key to be removed
	:return: deleted (key, value) pair
	"""


	try:
		del tree[key]
	except Exception:
		return None
	return None


def find(key: Any) -> Any:
	"""
	Find value by given key in the BST

	:param key: key for search in the BST
	:return: value associated with the corresponding key
	"""
	print(key)
	return None


def clear() -> None:
	"""
	Clear the tree

	:return: None
	"""
	global tree
	tree = {}
	return None
