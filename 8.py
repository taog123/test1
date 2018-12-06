# def test(x):
#     y1 = x+1
#     y2 = x+2
#     return y1,y2
#
# result = test(2)
# print(result)
# def test(name,*args):
#     print(name)
#     print(args)
#
# test("CodeScrew",*[1,2,3,4])

# def test(name,**kwargs):
# #     print(name)
# #     print(kwargs)
# #
# # test("CodeScrew",**{"x":1,"y":2})
# x=5
# def foo():
#     global x
#     y = x+1
#     x+=1
#     print(x)
# foo()

# def outer():
#     def inner():
#         print("innter")
#
#     inner()
# print("outer")
# x = 5
# def foo():
#     print(x)
# foo()
# x=5
# def foo():
#
#     x+=1
#     print(x)
# foo()
#
# def showplus(x):
#     print(x)
#     return (x)
#
# num = showplus(6)
# print(num)
# print(type(num))
#
# def outer():
#     def inner():
#         print("inner")
#     print("outer")
#     inner()
#
# outer()

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
