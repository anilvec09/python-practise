"""
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll
say is
the mean average of the values, except ignoring the largest and
smallest values in the array. If there are multiple copies of the
smallest value, ignore just one copy, and likewise for the
largest
value. Use int division to produce the final average. You may
assume
that the array is length 3 or more.
time took:   4:46 minutes
"""
def solution(input):
 # Code goes here
 max1 = max(input)
 min1 = min(input)

 input.remove(max1)
 input.remove(min1)

 sum = 0
 for i in input:
     sum = sum + i
 output = round(sum/len(input))
 # print(output)
 return output
assert solution([1, 2, 3, 4, 100]) == 3
assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution([-10, -4, -2, -4, -2, 0]) == -3