
# import time
# import  datetime
# def fn3(t):
#     def fn2(fn1):
#         def fn(*args,**kwargs):
#             start=datetime.datetime.now()
#             result=fn1(*args,**kwargs)
#             stop=datetime.datetime.now()
#             deltatime=((stop-start).total_seconds())
#             print(deltatime)
#             print("this func is {}".format('good' if deltatime<t else 'bad'))
#             return result
#         return fn
#     return fn2
# @fn3(2)
# def add(x,y):
#     time.sleep(2)
#     return x+y
#
# print(add(2,3))

import inspect
def wrps(fn):
    def wrapper(*args,**kwargs):
        sig = inspect.signature(fn)
        pam=sig.parameters
        print(pam)
        dictlist=list(pam.items())
        print(dictlist)

        for k,v in kwargs.items():
            if not isinstance(v,pam[k].annotation):
                print("{} is not ok".format(k))
        for index,value in enumerate(args):
            p, checktype = dictlist[index]
            if checktype.annotation is not inspect._empty and not isinstance(value,checktype.annotation):
                print("{} is not ok".format(p))

        result=fn(*args,**kwargs)

        return result
    return wrapper


@wrps

def add(x,y):
    return x+y
print(add(2.2,3))


# import inspect
# def wrapper(fn):
#     def wrap(*args,**kwargs):
#         sig=inspect.signature(fn) #取出函数的元素 例：def add（x:int,y:int）   取出的结果为(x:int,y:int）
#         print(sig)
#         parameters=sig.parameters #将上一步取出的函数的内容  转化为 有序字典  OrderedDict
#         print(parameters)
#         dictlist=list(parameters.items())#如果为位置参数，则将位置参数转化为列表方便判断   items。返回一个包含dict所有元素的list
#         print(dictlist)
#
#         for index,value in enumerate(args):  #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
#             print(args)
#
#             print(index,value)
#             p,checktype=dictlist[index] #参数解构
#             if not isinstance(value,checktype.annotation): #判断value值是不是int整型    位置参数
#                 print("{} is not ok".format(p))
#         for k, v in kwargs.items():
#             if not isinstance(v,parameters[k].annotation): #判断索引k所对应的V是不是整型    关键字参数
#                 print("{} is not ok".format(k))
#         result=fn(*args,**kwargs)
#         return result
#     return wrap
# @wrapper
# def add(x:int,y:int):
#     return x+y
# print(add(2,3.3))




