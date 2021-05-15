"""
Write a function that takes a number and returns a list of its
digits
"""
def solution(input):
    output = []
    temp = str(input)
 # Code goes here
    for i in range(0, len(temp)):
        output.append(temp[i])
    return output
assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]