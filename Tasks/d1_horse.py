# import numpy as np
from typing import Tuple


def calculate_paths(shape: Tuple[int, int], point: Tuple[int, int]) -> int:
    """
    Given field with size rows*cols count cells paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    # # Прямой способ (проходит 1 тест из 4-х)
    # steps = ((2, -1), (2, 1), (1, 2), (1, -2))
    # start = (0, 0)
    # visited = {start: 1}
    # stack = [start]
    # while stack:
    #     start = stack.pop(0)
    #     for route in steps:
    #         i = start[0] + route[0]
    #         j = start[1] + route[1]
    #         if i < shape[0] and 0 <= j < shape[1]:
    #             if (i, j) not in visited:
    #                 visited[(i, j)] = 2 * visited[start]
    #                 stack.append((i, j))
    #             else:
    #                 visited[(i, j)] += (2 * visited[start])
    # field = np.full(shape, 0)
    # # return visited[point]
    # for key, value in visited.items():
    #     field[key[0], key[1]] = value
    # return np.flipud(field)
    # if not point:
    #     return 0
    
    # Ленивая динамика
    if not point:
        return 0
    steps = ((-2, -1), (-2, 1), (-1, -2), (-1, 2))
    cells = [(), (), (), ()]
    for idx, step in enumerate(steps):
        i = point[0] + step[0]
        j = point[1] + step[1]
        if i >= 0 and 0 <= j < shape[1]:
            cells[idx] = (i, j)
    if point == (2, 1) or point == (1, 2):
        return 2
    return 2 * (calculate_paths(shape, cells[0]) + calculate_paths(shape, cells[1]) +
                calculate_paths(shape, cells[2]) + calculate_paths(shape, cells[3]))


if __name__ == '__main__':
    print(calculate_paths((9, 9), (8, 8)))
