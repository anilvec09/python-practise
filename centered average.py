def centered_average(nums):
    nums.remove(max(nums))
    nums.remove(min(nums))

    sum = 0
    for i in nums:
        sum += i

    return sum // len(nums)


assert centered_average([1, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
assert centered_average([-10, -4, -2, -4, -2, 0]) == -3