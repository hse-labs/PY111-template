def stairway_path(stairway: list) -> int:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	if len(stairway) > 2:
		for step in range(2, len(stairway)):
			one_step = stairway[step] + stairway[step - 1]
			two_steps = stairway[step] + stairway[step - 2]
			stairway[step] = (min(one_step, two_steps))
	elif len(stairway) == 2:
		return min(stairway)
	return stairway[-1]
