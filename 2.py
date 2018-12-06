# import random
# a=[]
# for c in range(10):
#     b=random.randint(1,10)
#     a.append(b)
# print(a)
# for i in range(9):
#     for j in range(0,9-i):
#         if a[j] > a[j - 1]:
#             a[j], a[j - 1] = a[j - 1], a[j]
#             b=a.sort()
#
# print(a)


# import random
# a=[]
# for i in range(10):
#     b = random.randint(1, 20)
#     a.append(b)
# print(a)
# for j in range(9):
#     for k in range(0,9-j):
#         if a[k] < a[k+1]:
#            a[k],a[k+1] = a[k+1],a[k]
# print(a)


# triger=[[1]]        # 杨辉三角
# pre=[1]
# for i in range(1,7):
#     cur=[1]
#     for j in range(1,len(pre)):
#         cur.append(pre[j-1]+pre[j])
#
#     cur.append(1)
#     triger.append(cur)
#     pre=cur.copy()
# print(triger)

# n=int(input(">>>"))
# m=int(input(">>>"))
# sum1=1
# sum2=1
# sum3=1
# for i in range(1,n):
#     sum1=sum1*i
# for j in range(1,m):
#     sum2=sum2*j
# for k in range(1,(n-m)):
#     sum3=sum3*k
# a=sum1/(sum2*sum3)
# print(a)

# n=int(input(">>>"))
# m=int(input(">>>"))
# a=1
# b=1
# c=1
# for i in range(1,n):
#     a=i*a
#     if (m-1)==i:
#         b=a
#     if (n-m)==i:
#         c=a
# print(a//(b*c))
#
