def avglength(s):
    if not s:
        return 0

    wc = 0

    for i in s.split():
        wc += len(i.replace(' ', ''))

    return wc / len(s.split())


assert avglength("i am good at doing") == 14/5
assert avglength("i am good at do   ing") == 14 / 6
assert avglength("") == 0

#
# def solution(input):
#     output = []
#     for i in range(0, len(input)):
#         if i % 2 != 0:
#             output.append(input[i])
#
#     return output
#
#
# assert solution([0, 1, 2, 3, 4, 5]) == [1, 3, 5]
# assert solution([1, -1, 2, -2]) == [-1, -2]


# def solution(input):
#     if not input:
#         return
#
#     for i in range(len(input)):
#         if i!=0 :
#             input[i] = input[i-1] + input[i]
#     print(input)
#     return input
#
#
# assert solution([1, 1, 1]) == [1, 2, 3]
# assert solution([1, -1, 3]) == [1, 0, 3]
#
