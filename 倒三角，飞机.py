# import random
# def fn(*args):
#     print(args)
#     return max(args),min(args)
# print(*fn(*[random.randint(0,10) for _ in range(5)]))
# def fn(n):
#     a = ' '.join([str(i) for i in range(n, 0, -1)])
#     b = len(a)
#     for i in range(1, n):
#         print("{:>{}}".format(" ".join([str(j) for j in range(i, 0, -1)]),b))
#     print(a)
# fn(12)
#
# def en(n):
#     c = ' '.join([str(i) for i in range(n, 0, -1)])
#     print(c)
#     for i in range(len(c)):
#         if c[i] == ' ':
#             print(' '*i, c[i+1:])
# en(12)
# # a=[]
# def fn(*args):
#     for i in args:
#         a.append(i)
#     print(max(a),min(a))
# fn(1,3,5,2)
# def ss(n):
#     for i in range(1,n+1):
#         a = []
#         for j in range(i,0,-1):
#             a.append(str("%2d"%j))
#         print(" "* 3*(n-i)+" ".join(a))
#     for i in range(n,0,-1):
#         a = []
#         for j in range(i,0,-1):
#             a.append(str("%2d" % j))
#         print(" "*3*(n-i)+" ".join(a))
# ss(12)


# def feiji():
#
#     for i in range(1,13):
#         for j in range(12,0,-1):
#             if j>i:
#                 print(' '*len(str(j)),end=' ')
#             else:
#                 print(j,end=' ')
#
#         print()
#
#
# def feiji2():
#     for i in range(1, 13):
#         for j in range(1,13):
#             if j < i:
#                 print(' '*len(str(13-j)),end=' ')
#             else:
#                 print(13-j, end=' ')
#
#         print()
# feiji()
# feiji2()