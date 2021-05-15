# def sum13(nums):
#     sum = 0
#     prev = None
#     for i in range(len(nums)):
#         if nums[i] != 13 and not prev == 13:
#             sum += nums[i]
#             prev = nums[i]
#         elif nums[i] == 13 or prev == 13:
#             prev = nums[i]
#             continue
#
#     return sum


def sum13(nums):
    prev = None
    sum = 0

    for i in nums:
        if i == 13 or prev == 13:
            prev = i
            continue
        if i != 13 and prev != 13:
            sum += i
            prev = i

    return sum


# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
#
#
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6