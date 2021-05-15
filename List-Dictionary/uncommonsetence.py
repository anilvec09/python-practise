def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    worda = A.split()
    wordb = B.split()

    res = []
    count = {}
    for i in worda:
        count[i] = count.get(i, 0) + 1
        if i not in wordb:
            res.append(i)

    for i in wordb:
        count[i] = count.get(i, 0) + 1
        if i not in worda:
            res.append(i)

    res2 = list(set(res))
    for i in res2:
        if count[i] > 1:
            res2.remove(i)

    return res2