def findchar(s, c):
    if not s or not c:
        return 0
    cnt = 0

    for i in s:
        if i == c:
            cnt += 1
    return cnt


assert findchar('mississipi', 's') == 4
assert findchar('mississipi', 'm') == 1
assert findchar('', '') == 0
