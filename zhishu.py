# num=int(input(">>>"))
# for i in range(2,num):
#     if num % i == 0:
#         print(" %d is not a prime number！" % num)
#         break
# else:
#     print(" %d is a prime number！" % num)
#
# for i in range(1, 10):
#         for k in range(1,i):
#             print (end="        ")
#         for j in range(i,10):
#             print('{}*{}={}'.format(j,i,i*j),end='\t')
#         print()

# a=[]
# for i in range(2,101):
#     for j in a :
#         if i%j ==0:
#             break
#     else:
#         a.append(i)
# print(a)
#


# import math
# a=[2]
# for i in range(2,101):
#     for j in a:
#         if i%j==0:
#             break
#         if j > int(math.sqrt(i)):
#             a.append(i)
#             break
# print(a)
#

# import random           #随机生成10个数，顺序排列
# a=[]
# for i in range(10):
#     # b = random.randint(1, 20)
#     a.append(random.randint(1,20))
# print(a)
# for j in range(9):
#     for k in range(0,9-j):
#         if a[k] < a[k+1]:
#            a[k],a[k+1] = a[k+1],a[k]
# print(a)


# triger=[[1]]            #杨辉三角
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