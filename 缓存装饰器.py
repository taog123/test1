#关键字参数
# def warrp(fn):
#     cache_dict={}
#     def cache(*args,**kwargs):
#         key=tuple(sorted([item for item in kwargs.items()]))
#         print(key)
#         if key not in cache_dict.keys():
#             result=fn(*args,**kwargs)
#             cache_dict[key]=result
#         return cache_dict[key]
#
#     return cache
#
#
# @warrp
#
#
# def add(x,y):
#     return x+y
# print(add(x=2,y=3))
# print(add(x=2,y=3))
# print(add(y=3,x=2))


#位置参数/关键字、默认参数
# import inspect
# import time
# def wraper(fn):
#     cache_dict={}
#     def fn1(*args,**kwargs):
#         key1_list=list(inspect.signature(fn).parameters)
#         print(key1_list)
#         key1_tuple=[(key1_list[i],v) for i,v in enumerate(args)]
#         print((key1_tuple))
#         key=tuple(sorted([item for item in kwargs.items()]+key1_tuple))
#         print(key)
#
#         if key not in cache_dict.keys():
#             result=fn(*args,**kwargs)
#             cache_dict[key]=result
#         return cache_dict[key]
#     return fn1
#
# @wraper
#
# def add(x,y=3):
#     time.sleep(3)
#     return x+y
#
# print(add(x=2,y=3))
# print(add(2,3))
# print(add(2,3))
# print(add(y=3,x=2))
# print(add(x=2,))


import time
import inspect
def wraper(fn):
    cache_dict={}
    def cache(*args,**kwargs):
        key_list=list(inspect.signature(fn).parameters)
        print(key_list)
        key_tuple=[(key_list[i],v) for i,v in enumerate(args)]
        print(key_tuple)
        key=tuple(sorted([item for item in kwargs.items()]+key_tuple))
        print(key)
        if key not in cache_dict.keys():
            result=fn(*args,**kwargs)
            cache_dict[key]=result
        return cache_dict[key]
    return cache

@wraper

def add(x,y=3):
    time.sleep(3)
    return x+y
print(add(2,3))
print(add(2,3))
print(add(y=3,x=2))
print(add(2,))
print(add(x=2,))



