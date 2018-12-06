# class Test:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
#     def fangfa(self):
#         c = self.a + self.b
#         return c
#
#
# a = Test(1, 2)
# b = a.fangfa()    # 要带括号，调用实例方法
# print(b)
class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def fangfa(self):
        c = self.a + self.b
        return c


a = Test(1, 2)
b = a.fangfa   # 不用带括号了
print(b)