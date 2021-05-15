
def removeDuplicates( nums) :
    for num in nums:
        while(nums.count(num) > 1):
            nums.remove(num)
    return len(nums)


assert removeDuplicates([1,1,2]) == 2
assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5