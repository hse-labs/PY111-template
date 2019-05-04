def stairway_path(stairway: list) -> int:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    # """
    # position = len(stairway) - 1
    # cost = stairway[-1]
    # while position > 1:
    #     if stairway[position - 2] != stairway[position - 1]:
    #         step = min(stairway[position - 2], stairway[position - 1])
    #         position -= (1 if step == stairway[position - 1] else 2)
    #     else:
    #         step = stairway[position - 2]
    #         position -= 2
    #     cost += step
    # cost += step
    available_steps = len(stairway)
    cost = stairway[-1]
    if available_steps == 1 or available_steps == 2:
        return cost
    else:
        step_cost = min(stairway[-3], stairway[-2])
        step = -1 if step_cost == stairway[-2] else -2
        if stairway[-3] == stairway[-2]:
            step = -2
        try:
            cost += stairway_path(stairway[:step])
        except TypeError:
            return None
        else:
            return cost


if __name__ == '__main__':
    step_costs = [5, 11, 43, 2, 23, 43, 22, 12, 6, 8]
    print(stairway_path(step_costs))

