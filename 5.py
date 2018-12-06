# a=[]
# for i in range(10):
#     a.append((i+1)**2)
# print(a)
#
# b=[(i+1)**2 for i in range(10)]
# print(b)

# a=[]
# for i in 'abcde':
#     for j in range(3):
#         a.append((i,j))
# print(a)

# a=[(i,j) for i in range(10) if i>5 for j in  range(10) if j>7]
# print(a)
#

# a=[(i) for i in range(20) if i%2==0 if i%3==0]
# print(a)

# a=[(i**2) for i in range(1,11) ]
# print(a)


# a=[1,2,4,16,2,5,10,15]
# b=[a[i]+a[i+1] for i in  range(len(a)-1)]
# print(b)


# [print('{}*{}={:<3}{}'.format(j,i,i*j,'\n'if i == j else ''),end = '') for i in range(1,10) for j in range(1,i+1)]

print("".join(['{}*{}={:<3}{}'.format(a,i,a*i, '\n'if i==a else ' ') for i in range(1,10) for a in range(1,i+1)]))
