def uniqueString(s):
    chars = []
    for i in range(0,len(s)):
        if s[i] in chars:
            return False
        chars.append(s[i])
    return True


assert uniqueString("abcd") == True
assert uniqueString("abccd") == False
assert uniqueString("aaaaad") == False