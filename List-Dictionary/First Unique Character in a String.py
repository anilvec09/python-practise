# https://leetcode.com/problems/first-unique-character-in-a-string/
def firstUniqChar(self, s: str) -> int:
    sam = Counter(s)
    for i in s:
        if sam[i] == 1:
            return s.index(i)
    return -1
