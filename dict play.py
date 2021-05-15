a='abc.asd.acsvg'
c={}
for i in range(len(a)):
     if c.get(a[i],0) == 0:
         c[a[i]] = a.count(a[i])
print(c)
print(len(c))
even ,odd = 0,0
for k,v in c.items():
    if v % 2 == 0:
        even +=1
    else:
        odd +=1
print(even,odd)