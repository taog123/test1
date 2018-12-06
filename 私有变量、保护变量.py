# class Test(object):
#
#     def __scolia__(self):   # 一个类似魔术方法，并不是私有化
#         return 'scolia'
#
#     def __good(self):   # 私有方法
#         return 'good'
#
# a = Test()
# print(Test.__dict__)
# print(a.__scolia__())  # 魔法方法可以在直接访问
# # print(a.__good())    # 私有方法不能直接访问
# print(a._Test__good())  # 强制访问