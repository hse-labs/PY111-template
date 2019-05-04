def stairway_path(stairway: list) -> int:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.
    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    for idx, cell in enumerate(stairway[::-1], 1):
        if idx == 2:
            stairway[-idx] += stairway[-idx + 1]
        elif idx > 2:
            stairway[-idx] += min(stairway[-idx + 1], stairway[-idx + 2])
    return min(stairway[0], stairway[1])
