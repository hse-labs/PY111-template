def stairway_path(stairway: list) -> int:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	if len(stairway) > 2:
		for i in range(2, len(stairway)):
			one_step = stairway[i] + stairway[i - 1]
			two_step = stairway[i] + stairway[i - 2]
			stairway[i] = (min(one_step, two_step))
	elif len(stairway) == 2:
		return min(stairway)
	return stairway[-1]