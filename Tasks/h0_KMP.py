from typing import Optional, Sequence


def kmp_algo(inp_string: str, substr: str) -> Optional(int):
	"""
	Implementation of Knuth-Morrison-Pratt algorithm

	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found
	"""

	def prefix_fun(prefix_str: str) -> Sequence[int]:
		"""
		Prefix function for KMP

		:param prefix_str: dubstring for prefix function
		:return: prefix values table
		"""
		print(prefix_str)
		return []

	print(inp_string, substr, prefix_fun)
	return None
