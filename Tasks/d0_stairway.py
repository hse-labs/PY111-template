def stairway_path(stairway: list) -> int:

	for i in range(2, len(stairway)):
		stairway[i] += min(stairway[i - 1], stairway[i - 2])

	return stairway[-1]
