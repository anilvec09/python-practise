def checkInclusion(s1: str, s2: str) -> bool:
    root = sorted(s1)
    for left in range(len(s2) - len(s1) + 1):
        window = s2[left: left + len(s1)]
        if sorted(window) == root:
            return True
    return False


assert checkInclusion("ab", "eidbaooo") == True
assert checkInclusion("ab", "eidboaoo") == False