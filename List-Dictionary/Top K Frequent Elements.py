# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent( nums, k:):
    c = sorted(Counter(nums).items(),key=lambda x:x[1],reverse=True)
    res = []
    for i in range(len(c)):
        if i < k:
            res.append(c[i][0])
    return res


def topKFrequent( nums, k) :
    return [i for i ,j in Counter(nums).most_common(k)]


