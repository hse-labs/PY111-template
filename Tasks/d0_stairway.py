def stairway_path(stairway: list) -> int:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	for i in range(2, len(stairway)):
		stairway[i] += min(stairway[i - 1], stairway[i - 2])
	return stairway[-1]
