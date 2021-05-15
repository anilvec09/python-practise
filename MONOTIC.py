def monotic(s):
    if not s or None in s:
        return None

    op = []
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            op.append(True)
        else:
            op.append(False)
    return False if False in op
    if not False in op:
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
             op.append(True)
        else:
            op.append(False)
    print(op)
    return False if False in op  else True

# def monotic(s):
#     if None in s:
#         return
#     n = sorted(s)
#     r = sorted(s,reverse=True)
#     print ( s , n , r)
#
#     return n == s or r == s





assert monotic([1,2,4,5,8,9]) == True
assert monotic([1,2,2,6,4,5,8,9]) == False
assert monotic([1,3,2,5,8,6]) == False
assert monotic([1,3]) == True
assert monotic([None,1]) == None
assert monotic([1,1,1,1,1,1]) == True