# from collections import Counter
# with open('e:/1/sample.txt',mode='r',encoding='utf-8') as f:
#     a=f.read()
#     b=a.split()
#     print(b)
#     print(Counter(b).most_common(10))


# with open('e:/1/sample.txt',mode='r',encoding='utf-8') as f:
#     a=f.read()
#     b=a.split()
#     c={}
#     for i in b:
#         if i not in c:
#             c[i]=1
#         else:
#             c[i]+=1
# d=sorted(c.items(),key=lambda x:x[1],reverse=True)
# print(d)
# e=[]
# for j in range(10):
#
#         e.append(d[j])
# print(e)

import re
with open('e:/1/sample.txt',mode='r',encoding='utf-8') as f:
    a=f.read()
    b=a.lower()
    g=re.sub('\W',' ',a).split()
    print(g)
    c={}
    for i in g:
        if i not in c:
            c[i]=1
        else:
            c[i]+=1
d=sorted(c.items(),key=lambda x:x[1],reverse=True)
print(d)
e=[]
for j in range(10):
    e.append(d[j])
print(e)













