# def fn(x):
#     return x**2
# a=map(fn,[1,2,3])
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# a=map(lambda x: x ** 2, [1, 2, 3, 4, 5])
# print(a)
# print(next(a))
# print(list(a))

# def fn(x):
#     return x%2==1
# a=filter(fn,[1,2,3,4,5])
# print(a)
# print(next(a))
# print(list(a))

# def f(x):
#     return True if x == 1 else False
# a=filter(lambda x: f(x), [-1, 0, 1])
# print(a)
# print(list(a))

# def fn(a,lists):
#     if lists is None:
#         yield  from a
#     else:
#         for b in a :
#             yield  a(b)
# c=fn(list[1,2,3,4,5])

import datetime
import time
def b(c):
    def a(fn1):
        def fn(*args,**wkargs):
            start = datetime.datetime.now()
            result=fn1(*args,**wkargs)
            end=datetime.datetime.now()
            deltatime=int((end-start).total_seconds())
            print(deltatime)
            print("this func is {}".format('good' if deltatime <c else 'bad'))
            return result
        return fn
    return a
@b(3)
def add(x,y):
    # time.sleep(2)
    return x+y
print(add(4,5))
