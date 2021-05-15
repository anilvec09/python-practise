# https://leetcode.com/problems/sort-characters-by-frequency/


def frequencySort(self, s: str) -> str:
    d= [s.count(i)*i for i in set(s)]
    return ''.join(sorted(d,key=len,reverse=True)  )


def frequencySort(self, s: str) -> str:
    d = {}
    op = ''
    for i in s:
        d[i] = d.get(i, 0) + 1
    t = [[v, k] for (k, v) in d.items()]
    print(t)
    t.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(t)):
        op += t[i][1] * t[i][0]
    return op
