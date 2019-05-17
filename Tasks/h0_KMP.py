from typing import Optional, List


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
	"""
	Implementation of Knuth-Morrison-Pratt algorithm

	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found
	"""

	def prefix_fun(prefix_str: str) -> List[int]:
		"""
		Prefix function for KMP

		:param prefix_str: dubstring for prefix function
		:return: prefix values table
		"""

		print(prefix_str)
		return []

	i = 0
	j = 0
	rez = None
	while i != len(inp_string):
		if inp_string[i] == substr[j] and j == len(substr) - 1:
			rez = i - j
			j = 0
			i += 1
		elif inp_string[i] == substr[j] and j < len(substr) - 1:
			i += 1
			j += 1
		elif inp_string[i] != substr[j] and j == 0:
			i += 1
		elif inp_string[i] != substr[j] and j > 0:
			i += 1
			j = 0
	print(inp_string, substr, prefix_fun)
	return rez


if __name__ == '__main__':
	print(kmp_algo("AAFAAFAAF", "AF"))
