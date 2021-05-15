# 1. count number of occurences each item/character of string:
nums=[2,3,2,1,1,1]
d= sorted([[i,nums.count(i)] for i in set(nums)],key=len,reverse=True)
# print(d) -> [[1, 3], [2, 2], [3, 1]]
counter = {i:s.count(i) for i in set(s)}
# 2. Dict to List and sort dict by values:
d = {"a" : 25 , "b" : 10 , "c" : 100 }
n = 1
sorted(d.items(),key=lambda x:x[1], reverse=True) /// sorted(d.items(),key=lambda x:x[1], reverse=True)[n-1]
# prtint() -> [('c', 100), ('a', 25), ('b', 10)] /// ('c', 100)

# 3. List to Dict
nums=[2,3,2,1,1,1]
for k,v in enumerate(nums):
    print(k,v)
# 0 2 -> 1 3 -> 2 2 -> 3 1 -> 4 1 -> 5 1

# 4. True -> 1 (RC)  False -> 0 (RC)
# True + False -> 1 + 0 = 1

# 5. uncommon words between two sentences
a="i am good"
b="i am very bad"
list(set(a.split()) ^ set(b.split()))
['bad', 'very', 'good']