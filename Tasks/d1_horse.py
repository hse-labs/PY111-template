
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
    field[1][2] = 2
    field[2][1] = 2

    for row in range(1, rows):
        for col in range(cols):
            if field[row][col] != 0:
                available_steps = [[row + 2, col - 1], [row + 1, col - 2], [row + 2, col + 1], [row + 1, col + 2]]
                for step in available_steps:
                    if 0 <= step[0] < rows and 0 <= step[1] < cols:
                        field[step[0]][step[1]] += 2 * field[row][col]
    return field[point[0]][point[1]]
