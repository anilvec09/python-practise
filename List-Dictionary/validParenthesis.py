def isValid(s: str) -> bool:
    stack = []
    charlist = ['(',  '{',  '[' ]
    for i in range (0, len(s)):
        if s[i] in charlist:
            stack.append(s[i])
        elif s[i] == ')' and  stack and stack[-1] == '('  :
            stack.pop()
        elif s[i] == '}' and  stack and stack[-1] == '{' :
            stack.pop()
        elif s[i] == ']' and  stack and stack[-1] == '['  :
            stack.pop()
        else: return False
    if stack : return False
    else: return True


assert isValid("()[]{}") == True
assert isValid("()") == True
assert isValid("(]") == False
assert isValid("([)]") == False
assert isValid("{[]}") == True

