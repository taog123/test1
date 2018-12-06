# import datetime
# import time
# def fn2(fn1):
#     def fn(*args,**kwargs):
#         start=datetime.datetime.now()
#         resault=fn1(*args,**kwargs)
#         stop=datetime.datetime.now()
#         deltatime=((stop-start).total_seconds())
#         print(deltatime)
#         print("this 函数 is {}".format('bad 'if deltatime>2 else 'good'))
#         return resault
#     return fn
# @fn2
# def add(x,y):
#     return x+y
# print(add(3,4))

# import time
# import datetime
# def fn3(t):
#     def fn2(fn1):
#         def fn(*args,**kwargs):
#             start=datetime.datetime.now()
#             resault=fn1(*args,**kwargs)
#             stop=datetime.datetime.now()
#             deltatime=((stop-start).total_seconds())
#             print(deltatime)
#             print("这个函数计算时间 {}".format('good' if deltatime<t else 'bad'))
#
#             return resault
#         return fn
#     return fn2
# @fn3(3)
# def add(x,y):
#     time.sleep(2)
#     return x+y
# print(add(2,3))
# import time
# import datetime
# def fn3(t):
#     def fn2(fn1):
#         def fn(*args,**kwargs):
#             start=datetime.datetime.now()
#             rsault=fn1(*args,**kwargs)
#             stop=datetime.datetime.now()
#             deltatime=((stop-start).total_seconds())
#             print(deltatime)
#             print("这个函数计算时间 {}".format('少' if deltatime<t else '多'))
#             return rsault
#         return fn
#     return fn2
# # @fn2
# @fn3(4)
# def add(x,y):
#     time.sleep(3)
#     return x*y
# print(add(8,9))























