
with open('e:/1/sample.txt',mode='r',encoding='utf-8') as f:
    a=(f.read())
    b=a.split()
    # print(b)
    c={}
    # for i in b:
        # print(i)
        # c[i]=c.get(i,0)+1

    for i in b:
        if i not in c:
            c[i]=1
        else:
            c[i]+=1
# print(c)
d=(sorted(c.items(), key=lambda s: s[1], reverse=True))
print(d)
e=[]
for j in range(10):
        e.append(d[j])
print(e)
