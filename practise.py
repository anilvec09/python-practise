# def maxarray(s):
#     s.sort()
#     return s[-1]
#
#
# assert maxarray([1,4,6,8,9,2,8]) == 9
# assert maxarray([1,4,6,1888,99,2,8]) == 1888
#
#
# def unmatch(s1,s2):
#     if not s1 or not s2:
#         return
#     output = []
#     for i in s1.split():
#         if i not in s2.split():
#             output.append(i)
#
#     for i in s2.split():
#         if i not in s1.split():
#             output.append(i)
#     return output
#
#
# assert unmatch("First this is first string", "second this is second string") == ['First','first','second', 'second']
#
#
# def avgwordlength(s):
#
#     if not s:
#         return
#     length = 0
#
#     for i in s.split():
#         length += len(i)
#
#     return (length/len(s.split()))
#
#
# assert avgwordlength("im go od bo ye") == 2
# assert avgwordlength("i am good bo y") == 10/5
#


# def monotic(s):
#     try:
#         if not s:
#             return
#
#         r,n = s
#         r.sort(reverse=True)
#         n.sort()
#
#         print(s,r,n)
#         if s == r or s == n:
#             return True
#         else:
#             return False
#     except:
#         print("I am here")
#         return False
#
#
# assert monotic([1,2,4,5,8,9]) == True
# assert monotic([1,3,2,5,8,6]) == False
# assert monotic([None,1]) == False
# monotic([1,2,4,5,8,9])



def validip(s):
    if not s:
        return

    print(s.count('.'))
    if s.count('.') != 3:
        return False

    for i in s.split('.'):
        if i > 255 or len(i) >3 or i[0] ==0 :
            return False
        else:
            return True


# assert validip("10.255.123.12") == True
# assert validip("0.00.00.123") == False
validip("0.00.00.123")