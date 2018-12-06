#
# class Feb:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#         self.c = [1]
#
#     def __call__(self, n, *args, **kwargs):
#         for i in range(n - 1):
#             sum = self.a + self.b
#             self.a = self.b
#             self.b = sum
#             self.c.append(sum)
#         print(self.c)
#         return self.c[n - 1]
#
# a = Feb()
# print(a(10))

class Feb:
    def __init__(self):
        self.x=1
        self.y=1
    def __call__(self,n):
        for i in range(n-1):
            self.x,self.y=self.y,self.x+self.y
            #self.x,self.y=self.y,self.x+self.y
        #下一步;self.x(这里的self.x就相当于上面等号后面的self.y),self.y(相当于上面等号后面的self.x+self.y)=self.y,self.x+self.y
        return self.x
a=Feb()
print(a(4))

