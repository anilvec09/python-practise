def replace(s):
    pos = None
    for i in range(len(s)):
        if s[i]:
            pos = i
            continue
        elif not s[i] and pos:
            s[i] = s[pos]
    return s

assert replace([None, None, 1, 2, None, None, 5, None]) == [None, None, 1, 2, 2, 2, 5, 5]
assert replace([None, None]) == [None , None]

def average(s):
    if not s:
        return False
    wl = 0
    for i in s:
        wl += len(i.replace(' ', ''))
    return wl / len(s)


assert average(["abc", "defg rth"]) == 10 / 2
assert average(["abcde", "ins  awe", "wijl   jll"]) == 18 / 3
def uncommon(s1, s2):
    op = []
    for i in s1.split():
        if i not in s2.split():
            op.append(i)
    for i in s2.split():
        if i not in s1.split():
            op.append(i)

    return op

assert uncommon("I am good boy", "i am bad boy") == ["I", "good", "i", "bad"]
assert uncommon("I am good boy", "") == ["I", "am", "good", "boy"]

def monotic(s):
    if None in s:
        return
    n = sorted(s)
    r = sorted(s,reverse=True)
    print ( s , n , r)

    return n == s or r == s

def moveZeroes(self, nums: List[int]) -> None:
    return nums.sort(key=lambda x: x == 0)

def end_other(a, b):
  if  a.lower().endswith(b.lower())  or b.lower().endswith(a.lower()):
    return True
  return False


assert end_other('Hiabc', 'abc') == True
assert end_other('Hiabc', 'abcd') == False

def isPalindrome( s: str) -> bool:
    a = ''.join([i for i in s if i.isalpha() or i.isdigit()]).lower()
    return a == a[::-1]

assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False

def twoSum( nums, target):
    d = {}
    for index, value in enumerate(nums):
        print(d)
        if target - value in d:
            return [d[target - value], index]
        else:
            d[value] = index

assert twoSum([2, 7, 11, 15], 9) == [0,1]