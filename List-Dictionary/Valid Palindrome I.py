def isPalindrome( s: str) -> bool:
    a = ''.join([i for i in s if i.isalpha() or i.isdigit()]).lower()
    return a == a[::-1]


assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False