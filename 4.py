# a,(b,c,d),e=[1,(2,3,4),5]
# _,(_,_,d),_=[1,(2,3,4),5]
# print(d)


# a='java_home=/usr/bin'
# print(a.split('='))

# import os
# path="/usr/bin/java_home"
# print(os.path.basename(path))
# print(os.path.dirname(path))


# import random
# a=[]
# b=[]
# for i in range(10):
#     c = random.randint(10, 20)
#     d = random.randint(10, 20)
#     a.append(c)
#     b.append(d)
# print(a)
# print(b)
# print(set(a)^set(b))
# f=(set(a)^set(b))
# print(len(f))
# print(set(a)&set(b))
# e=(set(a)&set(b))
# print(len(e))
# print(set(a)|set(b))
# g=((set(a)|set(b)))
# print(len(g))
#

import random
a=[]
for i in range(10):
    b=random.randint(1,20)
    a.append(b)
print(a)
for i in range(len(a)-1):      #i:0-9

    maxindex=-i-1
    for j in range(len(a)-i-1):
        if a[maxindex]<a[j]:
            maxindex=j
    a[-i-1],a[maxindex]=a[maxindex],a[-i-1]

print(a)
