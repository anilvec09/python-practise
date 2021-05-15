"""
Write a function that takes a number and returns a list of its
digits
Time Took: 7:40 minutes
"""
def solution(input):
    str1 = str(input)
    output = []
    for i in range(0, len(str1)):
        output.append(int(str1[i]))
    return output
assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]