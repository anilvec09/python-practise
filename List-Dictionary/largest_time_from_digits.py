import itertools
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        t = ""
        for p in itertools.permutations(arr):
            if (p[0]*10+p[1]) <24 and (p[2]*10+p[3]) <60:
                pt = f"{p[0]}{p[1]}:{p[2]}{p[3]}"
                if t != "":
                    t = max(t,pt)
                else:
                    t = pt
        return t