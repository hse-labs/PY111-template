from typing import Any
# import networkx as nx


def insert(key: Any, value: Any) -> None:
	"""
	Insert (key, value) pair to binary search tree

	:param key: key from pair (key is used for positioning node in the tree)
	:param value: value associated with key
	:return: None
	"""
	print(key, value)
	return None


def remove(key: Any) -> (Any, Any):
	"""
	Remove key and associated value from the BST

	:param key: key to be removed
	:return: deleted (key, value) pair
	"""
	print(key)
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
	return None
