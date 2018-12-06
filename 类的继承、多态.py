import math
class Shape:
    def __init__(self,n):
        self.n = n
    def mianji(self):
        raise error
class zheng(Shape):
    def mianji(self):
        mianji=self.n**2
        return mianji
class yuan(Shape):
    def mianji(self):
        mianji=self.n**2*math.pi
        return mianji
class san(Shape):
    def __init__(self,n,heigt):
        Shape.__init__(self,n)
        self.heigt=heigt
    def mianji(self):
        mianji=self.n*self.heigt/2
        return mianji
a=zheng(2)
print(a.mianji())
b=yuan(3)
print(b.mianji())
c=san(2,3)
print(c.mianji())
