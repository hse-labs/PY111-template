"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Hashable, Any, Optional, Tuple
# import networkx as nx


def insert(key: Hashable, value: Any) -> None:
	"""
	Insert (key, value) pair to binary search tree

	:param key: key from pair (key is used for positioning node in the tree)
	:param value: value associated with key
	:return: None
	"""
	print(key, value)
	return None


def remove(key: Hashable) -> Optional[Tuple[Hashable, Any]]:
	"""
	Remove key and associated value from the BST if exists

	:param key: key to be removed
	:return: deleted (key, value) pair or None
	"""
	print(key)
	return None


def find(key: Hashable) -> Optional[Any]:
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
