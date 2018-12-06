# import inspect
# def fn2(fn1):
#     def fn(*args,**kwargs):
#         sig=inspect.signature(fn1)
#         print(sig)
#         pam=sig.parameters
#         print(pam)
#         dictlist=list(pam.items())
#         print(dictlist)
#         for k,v in kwargs.items():
#             if not isinstance(v,pam[k].annotation):
#                 print("{} is not ok".format(k))
#         for index,value in enumerate(args):
#             p,checktype=dictlist[index]
#             if checktype.annotation is not inspect._empty and not isinstance(value,checktype.annotation):
#                 print("{} is not ok".format(p))
#
#         result=fn1(*args,**kwargs)
#         return result
#     return fn
# @fn2
#
#
# def add(x:int,y:int):
#     return x+y
# print(add(2,3.3))


# import inspect
# def fn2(fn1):
#     def fn(*args,**kwargs):
#         sig=inspect.signature(fn1)
#         print(sig)
#         pam=sig.parameters
#         print(pam)
#         dictlist=list(pam.items())
#         print(dictlist)
#         for k,v in kwargs.items():
#             if not isinstance(v,pam[k].annotation):
#                 print("{} is not ok".format(k))
#         for index,value in enumerate(args):
#             p,checktype=dictlist[index]
#             if checktype.annotation is not inspect._empty and not isinstance(value,checktype.annotation):
#                 print("{} is not ok".format(p))
#
#
#         result=fn1(*args,**kwargs)
#         return result
#
#     return fn
#
# @fn2
#
#
# def add(x,y):
#     return x+y
# print(add(2.2,3.3))



# import inspect
# def fn2(fn):
#     def fn1(*args,**kwargs):
#         sig=inspect.signature(fn)
#         pam=sig.parameters
#         dictlist=list(pam.items())
#         print(dictlist)
#         for k,v in kwargs.items():
#             if  not isinstance(v,pam[k].annotation):
#                 print("{} is not ok".format(k))
#         for index,value in enumerate(args):
#             p,checktype=dictlist[index]
#             if checktype.annotation is not inspect._empty and not isinstance(value,checktype.annotation):
#                 print(" {} is not ok".format(p))
#         reasult=fn(*args,**kwargs)
#         return reasult
#     return fn1
# @fn2
#
# def add(x,y):
#     return x+y
# print(add(2,3.3))




#自主完整版
import inspect
def fn2(fn):
    def fn1(*args,**kwargs):
        sig=inspect.signature(fn)
        pam=sig.parameters

        dictlist=list(pam.items())
        for k,v in kwargs.items():
            if not isinstance(v,pam[k].annotation):
                print("{} is not ok".format(k))
        for index,value in enumerate(args):
            p,checktype=dictlist[index]
            if checktype.annotation is not inspect._empty and not isinstance(value,checktype.annotation):
                print("{} is not ok".format(p))
        resault=fn(*args,**kwargs)
        return resault
    return fn1
@fn2

def add(x,y):
    return x+y
print(add(3.3,2))











