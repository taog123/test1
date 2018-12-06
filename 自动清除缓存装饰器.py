import inspect
import datetime
import time
# def costtime(fn):
#     def wrapper(*args,**kwargs):
#         start=datetime.datetime.now()
#         result=fn(*args,**kwargs)
#         end=datetime.datetime.now()
#         print('jjj',(end-start).total_seconds())
#         return result
#     return wrapper
# cache_dict={}         #公共缓存
def cache(fn):
    cache_dict = {}     #独立缓存
    def wrapper(*args,**kwargs):
        # gq_key=[]
        # for k,(_,stime) in cache_dict.items():
        #     print(cache_dict.items())
        #     deltatime=datetime.datetime.now().timestamp()-stime
        #     print(deltatime)
        #     if deltatime>0:
        #         gq_key.append(k)
        # for l in gq_key:
        #     cache_dict.pop(l)
        paras=list(inspect.signature(fn).parameters)
        print('hh',paras)
        para_tuple=[(paras[i],v) for i,v in enumerate(args)]
        print('dd',para_tuple)
        key=tuple(sorted([item for item in kwargs.items()]+para_tuple))
        print(key)
        if key not in cache_dict.keys():
            result=fn(*args,**kwargs)
            cache_dict[key]=(result,datetime.datetime.now().timestamp())
        return cache_dict[key][0]
    return wrapper

# @costtime
@cache
def add(x,y=2):
    time.sleep(1)
    return x+y
print(add(x=2,y=2))
print(add(2,2))


