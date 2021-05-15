def isPlanidromePermutation(s):
    char_dict = {}
    chars = []
    s = s.replace(' ', '')
    print(s)
    for i in range(0, len(s)):
        count = 1
        if s[i] in chars:
            count = char_dict[s[i]]
            count = count + 1
            char_dict[s[i]] = count
        else:
            char_dict[s[i]] = count
        chars.append(s[i])


    if len(s)%2 == 0:
        even = 0
        for i in char_dict.values():
            if i % 2 == 0:
                even = even + 1
        if even == len(char_dict.values()) :
            return True
        else:
            return False
    else:
        even = 0
        odd = 0
        for i in char_dict.values():
            if i % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        if odd != 1 and even != (len(char_dict.values()) - 1):
            return False
        else:
            return True


assert isPlanidromePermutation("tact coa") == True
assert isPlanidromePermutation("anilkumar") == False
assert isPlanidromePermutation("anil lnia") == True