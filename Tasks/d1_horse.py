import numpy as np
from typing import Tuple


def calculate_paths(shape: Tuple[int, int], point: Tuple[int, int]) -> int:
	"""
	Given field with size rows*cols count available paths from (0, 0) to point

	:param shape: tuple of rows and cols (each from 1 to rows/cols)
	:param point: desired point for horse
	:return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
	"""
	rows, cols = shape
	field = [[0 for _ in range(cols)] for _ in range(rows)]
	field[0][0] = 1

	for row in range(rows):
		for col in range(cols):
			if field[row][col] != 0:
				available_steps = [[row + 2, col - 1], [row + 1, col - 2], [row + 2, col + 1], [row + 1, col + 2]]
				for step in available_steps:
					if 0 <= step[0] < rows and 0 <= step[1] < cols:
						if field[step[0]][step[1]] > 0:
							field[step[0]][step[1]] += field[row][col]
						else:
							field[step[0]][step[1]] = 1
	return field[point[0]][point[1]]

