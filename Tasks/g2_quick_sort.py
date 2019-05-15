import random


def sort(nums):
	if len(nums) <= 1:
		return nums
	else:
		q = random.choice(nums)
	l_nums = [n for n in nums if n < q]

	e_nums = [q] * nums.count(q)
	b_nums = [n for n in nums if n > q]
	return sort(l_nums) + e_nums + sort(b_nums)
