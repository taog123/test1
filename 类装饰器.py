import datetime
import time
# def fn1(fn2):
#     def fn(*args,**kwargs):
#         start=datetime.datetime.now()
#           resault=fn2(*args,**kwargs)
#         end=datetime.datetime.now()
#         deltatime=((end-start)).total_seconds()
#         print(deltatime)
#         print("this 函数 is {}".format('bad ' if deltatime > 2 else 'good'))
#         return resault
#     return fn
# @fn1
# def add(x,y):
#     time.sleep(3)
#     return x+y
# print(add(2,3))
import datetime
import time
import functools
class Pp:
    def __init__(self,fn):
        self.fn=fn
        self.__name__=fn.__name__
        self.__doc__=fn.__doc__
        functools.wraps(self,fn)
    def __call__(self, *args, **kwargs):
        start=datetime.datetime.now()
        resault=self.fn(*args,**kwargs)
        end=datetime.datetime.now()
        print((end-start).total_seconds())
        return resault
@Pp   #add=Pp(add)

def add(x,y):
    "this ZPP"
    time.sleep(2)
    return x+y
print(add(2,3))
print(add.__doc__)
print(add.__name__)
