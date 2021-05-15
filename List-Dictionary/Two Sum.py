
def twoSum( nums, target):
    d = {}

    for index, value in enumerate(nums):
        print(d)
        if target - value in d:
            return [d[target - value], index]
        else:
            d[value] = index



assert twoSum([2, 7, 11, 15], 9) == [0,1]