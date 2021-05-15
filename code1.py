"""
Write a function that returns the cumulative sum of elements in a
list
time took : 6:40 minutes
"""
def solution(input):
    sum = 0
    output = []
    for i in range (0, len(input)):
        if i != 0:
            sum = sum + input[i]
            print(sum)
            output.append(sum)
        else:
            sum = sum + input[i]
            output.append(input[i])
    print(output)
    return output

assert solution([1,1,1]) == [1,2,3]