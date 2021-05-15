def sum67(nums):
  flag = False
  sum = 0

  for num in nums:
    if (num == 6):  # Turn the flag on if the number is 6
      flag = True
      continue
    if (num == 7 and flag is True):  # Turn the flag Off when 7 is seen after 6
      flag = False
      continue
    if (flag is False):  # Keep on adding the nums otherwise
      sum += num
  return sum





assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5
assert sum67([1, 2, 2]) == 5
assert sum67([1, 1, 6, 7, 2]) == 4
assert sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) == 2